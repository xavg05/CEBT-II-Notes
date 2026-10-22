"""Verify the Reaction Engineering II section 2 results (RE-07 to RE-12).

Needs sympy, numpy and scipy on PYTHONPATH (the portable interpreter lacks them).
Writes other/work/progress/re-s2-verification.json.
"""
from pathlib import Path
import json, os, sys
if os.environ.get('RE_PYLIB'):
    sys.path.insert(0, os.environ['RE_PYLIB'])
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[3]
out = {}

r, R, rc, t, tau = sp.symbols('r R r_c t tau', positive=True)
rho, C, D, De, kg, ksa, nA, nB = sp.symbols('rho_m C D D_e k_g k_SA nu_A nu_B', positive=True)

# RE-07: film control, Stokes regime (Sh = 2 so k_g = D/r).
# -4 pi r^2 rho dr/dt = 4 pi r^2 k_g C nu_A/nu_B
lhs = sp.integrate(-r, (r, R, r))
rhs = D * C * nA / (rho * nB) * t
t_film = sp.solve(sp.Eq(lhs, rhs), t)[0]
tau_film = sp.simplify(t_film.subs(r, 0))
assert sp.simplify(tau_film - R**2 * rho * nB / (2 * D * C * nA)) == 0
x = sp.symbols('x', positive=True)  # x = t/tau
r_of_x = R * sp.sqrt(1 - x)
assert sp.simplify(t_film.subs(r, r_of_x) / tau_film - x) == 0
out['RE-07'] = {'tau_c': str(tau_film), 'r/R': 'sqrt(1-t/tau)', 'X': '1-(1-t/tau)^(3/2)'}

# RE-08: reaction control, and film + reaction in series (Stokes regime).
t_rxn = sp.solve(sp.Eq(R - r, nA * ksa * C / rho * t), t)[0]
tau_rxn = t_rxn.subs(r, 0)
assert sp.simplify(tau_rxn - R * rho / (nA * ksa * C)) == 0
# series: dr/dt = -(nA/nB) C/rho / (r/D + 1/(nB ksa))
t_series = sp.integrate((nB / (nA * C)) * rho * (r / D + 1 / (nB * ksa)), (r, r, R))
assert sp.simplify(t_series - (t_film + t_rxn)) == 0
out['RE-08'] = {'tau_c': str(tau_rxn), 'series_time_is_sum': True,
                'film_to_reaction_resistance_ratio': 'nu_B k_SA r / D'}

# Plot readings for the shrinking-particle comparison.
xs = np.array([0.25, 0.5, 0.75])
out['RE-08']['X_film'] = dict(zip(map(str, xs), np.round(1 - (1 - xs)**1.5, 3).tolist()))
out['RE-08']['X_reaction'] = dict(zip(map(str, xs), np.round(1 - (1 - xs)**3, 3).tolist()))

# RE-09: shrinking core, internal (product-layer) diffusion control.
a, b = sp.symbols('a b')
Cprof = a / r + b
sol = sp.solve([Cprof.subs(r, R) - C, Cprof.subs(r, rc)], [a, b])
Cprof = Cprof.subs(sol)
assert sp.simplify(Cprof - C * (1 / r - 1 / rc) / (1 / R - 1 / rc)) == 0
flux_in = sp.simplify(De * sp.diff(Cprof, r) * 4 * sp.pi * r**2)
assert sp.simplify(sp.diff(flux_in, r)) == 0  # same at every radius
assert sp.simplify(flux_in - 4 * sp.pi * De * C * R * rc / (R - rc)) == 0
s = sp.symbols('s', positive=True)
integral = sp.integrate((1 / R - 1 / s) * s**2, (s, R, rc))
expr = sp.expand(6 * integral / R**2)
y = sp.symbols('y', positive=True)  # y = r_c/R
assert sp.simplify(expr.subs(rc, y * R) - (2 * y**3 - 3 * y**2 + 1)) == 0
tau_ash = rho * R**2 * nB / (6 * De * C * nA)
out['RE-09'] = {'flux_in': str(flux_in), 'tau_c': str(tau_ash),
                't/tau': '2(rc/R)^3-3(rc/R)^2+1 = 1-3(1-X)^(2/3)+2(1-X)'}
Xs = sp.symbols('X', positive=True)
assert sp.simplify((2 * y**3 - 3 * y**2 + 1).subs(y, (1 - Xs)**sp.Rational(1, 3))
                   - (1 - 3 * (1 - Xs)**sp.Rational(2, 3) + 2 * (1 - Xs))) == 0
# Early-time behaviour: X ~ sqrt(t) for product-layer control.
eps = sp.symbols('epsilon', positive=True)
early = sp.series((1 - 3 * (1 - eps)**sp.Rational(2, 3) + 2 * (1 - eps)), eps, 0, 3).removeO()
out['RE-09']['early_t_over_tau'] = str(sp.simplify(early))  # eps^2/3

# RE-10: film control with constant particle size; three resistances in series.
tau_core_film = rho * R * nB / (3 * kg * C * nA)
# -d(4/3 pi rc^3 rho)/dt = nA/nB 4 pi R^2 kg C  -> X = t/tau
dXdt = sp.simplify((nA / nB) * 4 * sp.pi * R**2 * kg * C / (sp.Rational(4, 3) * sp.pi * R**3 * rho))
assert sp.simplify(1 / dXdt - tau_core_film) == 0
out['RE-10'] = {'tau_film': str(tau_core_film)}


def solve_X(fun, xq):
    return brentq(lambda X: fun(X) - xq, 0, 1)


f_ash = lambda X: 1 - 3 * (1 - X)**(2 / 3) + 2 * (1 - X)
f_rxn = lambda X: 1 - (1 - X)**(1 / 3)
out['RE-10']['X_at_half_tau'] = {
    'film': 0.5,
    'reaction': round(solve_X(f_rxn, 0.5), 3),
    'internal_diffusion': round(solve_X(f_ash, 0.5), 3)}
cross = brentq(lambda X: f_ash(X) - f_rxn(X), 0.3, 0.99)
out['RE-10']['ash_reaction_curves_cross'] = {'X': round(cross, 3), 't_over_tau': round(f_rxn(cross), 3)}

# Numerical check of time additivity with all three resistances acting together.
p = dict(R=1e-3, rho=2e4, C=1.0, kg=0.05, De=2e-6, ksa=0.02, nA=1.0, nB=1.5)
def rhs_core(_, z):
    rcv = max(z[0], 1e-12)
    res = (1 / (4 * np.pi * p['R']**2 * p['kg'])
           + (1 / rcv - 1 / p['R']) / (4 * np.pi * p['De'])
           + 1 / (p['nB'] * 4 * np.pi * rcv**2 * p['ksa']))
    NB = p['C'] / res
    return [-(p['nA'] / p['nB']) * NB / (4 * np.pi * rcv**2 * p['rho'])]
taus = {
    'film': p['rho'] * p['R'] * p['nB'] / (3 * p['kg'] * p['C'] * p['nA']),
    'ash': p['rho'] * p['R']**2 * p['nB'] / (6 * p['De'] * p['C'] * p['nA']),
    'rxn': p['R'] * p['rho'] / (p['nA'] * p['ksa'] * p['C'])}
target = 0.9
yq = (1 - target)**(1 / 3) * p['R']
ev = lambda _, z: z[0] - yq
ev.terminal = True
sol = solve_ivp(rhs_core, [0, 1e7], [p['R']], events=ev, rtol=1e-10, atol=1e-16)
t_num = sol.t_events[0][0]
t_sum = taus['film'] * target + taus['ash'] * f_ash(target) + taus['rxn'] * f_rxn(target)
out['RE-10']['additivity_check'] = {'t_numeric_s': round(t_num, 3), 't_sum_s': round(t_sum, 3),
                                    'relative_difference': float(abs(t_num - t_sum) / t_sum)}
assert abs(t_num - t_sum) / t_sum < 1e-6

# RE-11: droplet evaporation. Heat balance with Sh = Nu gives D Psat/(RT) dH = lambda (T0 - T).
Rg = 8.314462618
dH = 44.0e3  # J/mol, water near 298 K, assumed constant
P298 = 3169.9  # Pa, water vapour pressure at 298.15 K
Dw = 2.6e-5  # m2/s, water vapour in air near 300 K
lam = 0.026  # W/m/K, air near 300 K
Psat = lambda T: P298 * np.exp(-dH / Rg * (1 / T - 1 / 298.15))
T0 = 323.15
Ts = brentq(lambda T: Dw * Psat(T) / (Rg * T) * dH - lam * (T0 - T), 250, T0)
ratio = (Psat(Ts) / Ts) / (Psat(T0) / T0)
out['RE-11'] = {'T0_K': T0, 'surface_T_K': round(Ts, 2), 'surface_T_C': round(Ts - 273.15, 1),
                'evaporation_rate_ratio_vs_uniform_T0': round(ratio, 3),
                'properties': {'dH_J_per_mol': dH, 'Psat_298_Pa': P298, 'D_m2_s': Dw, 'lambda_W_mK': lam}}
# Sh/Nu ratio under Ranz-Marshall-type correlations at large Re: (Sc/Pr)^(1/3)
Sc, Pr = 0.60, 0.71
out['RE-11']['Sc_over_Pr_cuberoot'] = round((Sc / Pr)**(1 / 3), 3)
# Size independence: k_g and h both scale as 1/d at Sh = Nu = 2, so the balance has no radius.
out['RE-11']['size_independent'] = True

# RE-12: mean conversion of segregated particles with a mixed-solids (exponential) RTD.
from scipy.integrate import quad
X_of = {
    'film_core': lambda s: s,
    'reaction': lambda s: 1 - (1 - s)**3,
    'internal_diffusion': lambda s: brentq(lambda X: f_ash(X) - s, 0, 1) if s < 1 else 1.0,
}
def unconverted_mixed(name, T):  # T = mean solid residence time / tau_c
    val, _ = quad(lambda s: (1 - X_of[name](s)) * np.exp(-s / T) / T, 0, 1, limit=200)
    return val
asym = {k: quad(lambda s: 1 - X_of[k](s), 0, 1, limit=200)[0] for k in X_of}
needed = {k: brentq(lambda T: unconverted_mixed(k, T) - 0.01, 0.1, 1e4) for k in X_of}
out['RE-12'] = {
    'large_mean_time_unconverted_coefficient': {k: round(v, 4) for k, v in asym.items()},
    'mean_time_over_tau_for_99pct_mixed_solids': {k: round(v, 1) for k, v in needed.items()},
    'mean_time_over_tau_for_99pct_plug_solids': {
        'film_core': 0.99, 'reaction': round(1 - 0.01**(1 / 3), 3),
        'internal_diffusion': round(f_ash(0.99), 3)},
}

# RE-07 quasi-steady justification: solid inventory vs gas reagent concentration (carbon in air).
rho_carbon = 2000 / 0.012  # mol/m3 for a 2000 kg/m3 carbon particle
C_O2 = 0.21 * 101325 / (Rg * 1000)  # mol/m3 in air at 1000 K
out['RE-07']['rho_m_over_C_carbon_in_air_1000K'] = round(rho_carbon / C_O2)
# RE-08 initial slopes dX/d(t/tau): film 3/2, reaction 3.
s_ = sp.symbols('s')
out['RE-08']['initial_slopes'] = {
    'film': float(sp.diff(1 - (1 - s_)**sp.Rational(3, 2), s_).subs(s_, 0)),
    'reaction': float(sp.diff(1 - (1 - s_)**3, s_).subs(s_, 0))}
out['RE-11']['rate_reduction_factor'] = round(1 / ratio, 2)

dest = ROOT / 'other/work/progress/re-s2-verification.json'
dest.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
