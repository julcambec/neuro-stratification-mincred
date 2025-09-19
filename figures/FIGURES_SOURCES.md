# Figures — Sources, Provenance, and Compliance Notes

This repository reuses **aggregate-level** visuals from the author's MSc manuscript and includes synthetic placeholders for demo outputs. No ABCD subject-level data, IDs, or model parameters trained on ABCD are included.

---

## Thesis Figures

### Figure 4 — Regional Neuroimaging Signatures
- **Repo file:** `figures/figure4_brain_signatures.jpg`
- **Origin:** Author’s MSc dissertation (Section: Results; Figure 4).
- **Data type:** Aggregated group-level effect sizes (Cohen’s d) with FDR correction.
- **Compliance note:** Contains **no** subject-level rows, IDs, or predictions. Displays only cohort-level summaries.

### Figure 5 — CBCL Trajectories
- **Repo file:** `figures/figure5_cbcl_trajectories.jpg`
- **Origin:** Author’s MSc dissertation (Section: Results; Figure 5).
- **Data type:** Aggregated average CBCL internalizing/externalizing trajectories (baseline, 3-year).
- **Compliance note:** Group means only; **no** individual trajectories.

---

## Synthetic Placeholders (to be overwritten by pipeline)

### Bootstrap Stability (ARI)
- **Repo file:** `figures/fig_stability_ari.png`
- **Purpose:** Visual scaffold for README until `make demo_stratify` produces run-specific outputs.
- **Compliance note:** Fully synthetic.

### Feature Importance (SHAP/Permutation)
- **Repo file:** `figures/fig_shap_top10.png`
- **Purpose:** Visual scaffold for README until `make demo_baselines` produces run-specific outputs.
- **Compliance note:** Fully synthetic.

---

## License and Reuse
- **Thesis-derived visuals:** © The author. Reused here for portfolio demonstration under fair academic use; do not redistribute outside this repository without permission. See LICENSE for repo terms; thesis may carry additional institutional terms.
- **Synthetic placeholders:** May be reused within this repo and overwritten by pipeline runs.

## DUA Compliance (figures)
- No ABCD subject-level data.
- No ABCD-trained weights/hyperplanes or site harmonization parameters.
- Only aggregated summaries and synthetic visuals are present.
