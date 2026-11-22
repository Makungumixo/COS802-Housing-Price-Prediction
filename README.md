# COS802 — Housing Price Prediction with Regression and Feature Importance Analysis

## Objective
This project investigates how domain-informed feature engineering and regression model choice affect housing-price prediction and interpretability using the Ames Housing dataset.

## Research questions
- **RQ1:** How accurately can housing sale prices be predicted using the original structured features?
- **RQ2:** To what extent does domain-informed feature engineering improve prediction compared with the original features?
- **RQ3:** How does predictive performance differ across linear, bagging-based and boosting-based regression?
- **RQ4:** Which property characteristics most influence predictions, and how do their effects vary across individual predictions?

## Experimental protocol
The 2,930 observations are split once using `random_state=16153970`: 2,344 development observations and 586 locked test observations. Five fixed folds within development support model comparison and tuning. Preprocessing is fitted only on training data within each fold. RMSE is the primary development-selection metric.

The frozen final held-out engineered-XGBoost result is **MAE $13,885.15; RMSE $25,354.31; R² 0.8999**. Bootstrap 95% intervals are approximately **MAE $12,372–$15,772; RMSE $18,165–$34,407; R² 0.840–0.941**.

## Reproduce the analysis
Reference environment: Google Colab, Python 3.11+.

1. Mount Google Drive.
2. Keep the project at `/content/drive/MyDrive/MIT BIG DATA SCIENCE/COS802_PROJECT/`.
3. Confirm `data/raw/AmesHousing.txt` exists.
4. Install dependencies with `pip install -r requirements.txt` when compatible packages are not already available.
5. Run notebooks **01 → 06 in numerical order**.
6. Do not use Notebook 06 or any test-set observation to reopen final model selection.

| Notebook | Purpose | RQ |
|---|---|---|
| `01_data_audit_eda.ipynb` | Audit, early split, development-only target EDA, supplementary clustering/PCA | Context |
| `02_preprocessing_feature_engineering.ipynb` | Missingness semantics, preprocessing, engineered features, fixed folds | RQ2 |
| `03_baseline_models.ipynb` | Naive/Ridge baselines and raw/log target comparison | RQ1, RQ2 |
| `04_model_comparison.ipynb` | Ridge vs Random Forest vs XGBoost using development CV | RQ3 |
| `05_interpretability_error_analysis.ipynb` | Frozen test evaluation, bootstrap CIs, residual/subgroup analysis, SHAP | RQ4 |
| `06_robustness_sensitivity_analysis.ipynb` | Sale-context sensitivity and engineered-feature ablation, development only | RQ2 |

## Canonical reusable code
Reusable logic lives in `src/`: `config.py`, `features.py`, `preprocessing.py`, and `evaluation.py`.

In Colab, add the **project root**, not the `src` directory, to `sys.path`:

```python
import os, sys
PROJECT_DIR="/content/drive/MyDrive/MIT BIG DATA SCIENCE/COS802_PROJECT"
os.chdir(PROJECT_DIR)
if PROJECT_DIR not in sys.path:
    sys.path.insert(0,PROJECT_DIR)

from src.config import SEED,TARGET
from src.features import AmesFeatureEngineer,validate_engineered_features
from src.preprocessing import build_preprocessor
from src.evaluation import regression_metrics
```

`src` is a Python package because it contains `__init__.py`. This import pattern avoids the Colab import problem encountered when `src` itself was placed on `sys.path`.

## Validation and leakage controls
- `Order` and `PID` are excluded from modelling.
- The train/test split precedes target-informed EDA.
- The final model was selected using development CV. Notebook 06 is a post-hoc follow-up motivated by test-set SHAP; it does not revise the frozen model.
- Imputation, encoding and scaling are fitted within training folds.
- Structural absence is represented explicitly where appropriate.
- Engineered features are checked for existence, finite/non-negative values where applicable, and binary amenity flags.
- Feature-column alignment can be asserted before evaluation.
- Notebook 06 is development-only and cannot redefine the frozen final model.

## Engineered-feature robustness
For frozen XGBoost development CV, all engineered features achieved RMSE **$22,195** and R² **0.922**. Removing all engineered features increased RMSE by **3.75%**. Removing `QualLivArea` increased RMSE by **2.06%**, removing `TotalSF` by **1.22%**, and removing both by **4.35%**.

Removing `Sale Type` and `Sale Condition` changed development CV RMSE from **$22,195 to $22,265** (about **+0.32%**).

## Deliverables
- [Current project report (PDF)](reports/u16153970_Ndlovu%20M_COS802%20Report.pdf).
- [Current presentation (PowerPoint)](presentation/Ndlovu%20Makungu_u16153970_COS802.pptx).

The current report and presentation are the author-supplied files, preserved without content changes.

## Methodological notes
Notebook 04 changes structural-absence handling as well as adding ten features in the engineered arm. Its results compare complete pipelines and cannot isolate the effect of feature creation alone. Notebook 06 retains the absence handling during feature removal, but is post-hoc and was motivated by test-set SHAP; it is exploratory rather than independent confirmation.

Notebook 04 uses development CV for tuning/model selection, so those CV scores are not an independent final performance estimate. Notebook 05's held-out test is the independent final evaluation. SHAP describes how the fitted model uses predictors and must not be interpreted causally. Small subgroup results should be interpreted cautiously.

## Project structure
```text
COS802_PROJECT/
├── data/
│   ├── raw/
│   ├── processed/
│   └── splits/
├── notebooks/
│   ├── 01_data_audit_eda.ipynb
│   ├── 02_preprocessing_feature_engineering.ipynb
│   ├── 03_baseline_models.ipynb
│   ├── 04_model_comparison.ipynb
│   ├── 05_interpretability_error_analysis.ipynb
│   └── 06_robustness_sensitivity_analysis.ipynb
├── src/
├── reports/
├── presentation/
├── README.md
└── requirements.txt
```

## Dataset
Ames Housing contains 2,930 residential property sales and 82 columns including `SalePrice`. The raw project file is `data/raw/AmesHousing.txt`.

Primary reference: Dean De Cock (2011), *Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project*, Journal of Statistics Education, 19(3), DOI 10.1080/10691898.2011.11889627.

**Random seed:** `16153970`. Preserve the saved train/test split and development-fold membership files when reproducing reported results.

## Reproducibility status
Executed notebooks and saved outputs preserve the reported experiment. Packaging for GitHub did not rerun model training. Dependency ranges describe the reference environment, not an exact lockfile. The notebooks and `src/config.py` retain their original Colab/Drive paths; copy this repository into the documented Drive location before running. A local run requires adapting those paths and Drive-mount cells.

## Data attribution
The dataset belongs to its original authors; inclusion does not assign it a new license. See [data provenance](data/README.md). No blanket software or dataset license is granted by this repository.
