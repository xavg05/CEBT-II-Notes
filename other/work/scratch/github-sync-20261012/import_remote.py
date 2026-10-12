import datetime, hashlib, itertools, json, subprocess
from pathlib import Path

BASE = Path(__file__).parent
def git(*args, data=None):
    return subprocess.check_output(['git', *args], input=data).decode().strip()

for blob in json.loads((BASE/'blobs.json').read_text()):
    sha = git('hash-object', '-w', '--stdin', data=blob['content'].encode())
    assert sha == blob['sha'], (sha, blob['sha'])

remote = json.loads((BASE/'remote-tree.json').read_text())
entries = remote['tree']
directories = {x['path']: x['sha'] for x in entries if x['type']=='tree'}
directories[''] = remote['sha']
for directory, expected in sorted(directories.items(), key=lambda x: x[0].count('/') + bool(x[0]), reverse=True):
    records = []
    for entry in entries:
        parent, _, name = entry['path'].rpartition('/')
        if parent == directory:
            records.append(f"{entry['mode']} {entry['type']} {entry['sha']}\t{name}".encode()+b'\0')
    sha = git('mktree', '-z', data=b''.join(records))
    assert sha == expected, (directory,sha,expected)

def import_commit(commit):
    def ident(role, zone):
        who=commit[role]
        epoch=int(datetime.datetime.fromisoformat(who['date'].replace('Z','+00:00')).timestamp())
        return f"{role} {who['name']} <{who['email']}> {epoch} {zone}"
    for zones, newline in itertools.product(itertools.product(['+0000','+0100','-0000'],repeat=2), ['', '\n']):
        lines=[f"tree {commit['tree']['sha']}"]
        lines += [f"parent {p['sha']}" for p in commit['parents']]
        lines += [ident('author',zones[0]),ident('committer',zones[1])]
        data=('\n'.join(lines)+'\n\n'+commit['message']+newline).encode()
        sha=hashlib.sha1(b'commit '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if sha==commit['sha']:
            assert git('hash-object','-t','commit','-w','--stdin',data=data)==sha
            return sha
    raise RuntimeError('Cannot reconstruct commit '+commit['sha'])

for commit in json.loads((BASE/'commits.json').read_text()):
    print('Imported commit',import_commit(commit))
print('Imported and verified complete remote tree',remote['sha'])
