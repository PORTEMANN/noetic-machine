#!/usr/bin/env python3
"""
Analyse officielle du benchmark B1-rotation (protocole fige 2b6a1e00...).
Fit lineaire de atan2(yv, xv) deroule sur t in [100, 600] ; verdicts P1-P4.
"""
import pickle
import numpy as np
import json

CFGS = [("om000", 0.0), ("om010", 0.010), ("om020", 0.020)]
runs, omega_mes, dE_max, dL_max = {}, {}, {}, {}

for cfg, om in CFGS:
    d = pickle.load(open(f"b1_{cfg}.pkl", "rb"))
    runs[om] = d
    phi = np.unwrap(np.arctan2(d["yv"], d["xv"]))
    m = d["t"] >= 100.0
    pente, _ = np.polyfit(d["t"][m], phi[m], 1)
    omega_mes[om] = pente
    dE = np.abs(d["e_rot"] - d["e_rot"][0]) / abs(d["e_rot"][0])
    dL = np.abs(d["lz"] - d["lz"][0]) / abs(d["lz"][0])
    dE_max[om], dL_max[om] = float(dE.max()), float(dL.max())

oms = np.array(sorted(omega_mes))
w = np.array([omega_mes[o] for o in oms])
w_p0 = float(w[oms == 0.0][0])
slope, intercept = np.polyfit(oms, w, 1)
ecarts = np.abs(w - (w_p0 - oms)) / abs(w_p0)

verdicts = {
    "P1_loi_de_frame": bool(np.all(ecarts <= 0.10) and (-1.10 <= slope <= -0.90)),
    "P2_fenetre_fetter": bool(0.012 <= w_p0 <= 0.045),
    "P3_signe": bool(w_p0 > 0),
    "P4_conservation": bool(max(dE_max.values()) <= 0.01 and max(dL_max.values()) <= 0.01),
}

out = {
    "omega_mes": {str(o): float(omega_mes[o]) for o in oms},
    "omega_p0": w_p0,
    "pente_fit": float(slope), "ordonnee_fit": float(intercept),
    "ecarts_relatifs": {str(o): float(e) for o, e in zip(oms, ecarts)},
    "dE_max": dE_max, "dL_max": dL_max,
    "verdicts": verdicts, "toutes_confirmees": bool(all(verdicts.values())),
}
print(json.dumps(out, indent=2, ensure_ascii=False))
json.dump(out, open("b1_verdicts.json", "w"), indent=2, ensure_ascii=False)
