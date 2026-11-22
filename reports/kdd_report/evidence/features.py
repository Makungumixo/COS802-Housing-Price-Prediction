"""Domain-informed feature engineering and validation for Ames Housing."""
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
STRUCTURAL_NONE_COLS=["Alley","Mas Vnr Type","Bsmt Qual","Bsmt Cond","Bsmt Exposure","BsmtFin Type 1","BsmtFin Type 2","Fireplace Qu","Garage Type","Garage Finish","Garage Qual","Garage Cond","Pool QC","Fence","Misc Feature"]
ENGINEERED_FEATURES=["HouseAge","RemodAge","TotalSF","TotalBathrooms","TotalPorchSF","HasGarage","HasBasement","HasFireplace","HasPool","QualLivArea"]
def apply_structural_absence(X):
    X=X.copy()
    for c in STRUCTURAL_NONE_COLS:
        if c in X.columns: X[c]=X[c].fillna("None")
    return X
class AmesFeatureEngineer(BaseEstimator,TransformerMixin):
    def fit(self,X,y=None): return self
    def transform(self,X):
        X=apply_structural_absence(X)
        X["HouseAge"]=(X["Yr Sold"]-X["Year Built"]).clip(lower=0)
        X["RemodAge"]=(X["Yr Sold"]-X["Year Remod/Add"]).clip(lower=0)
        X["TotalSF"]=X[["Total Bsmt SF","1st Flr SF","2nd Flr SF"]].fillna(0).sum(axis=1)
        b=X[["Full Bath","Half Bath","Bsmt Full Bath","Bsmt Half Bath"]].fillna(0)
        X["TotalBathrooms"]=b["Full Bath"]+.5*b["Half Bath"]+b["Bsmt Full Bath"]+.5*b["Bsmt Half Bath"]
        X["TotalPorchSF"]=X[["Open Porch SF","Enclosed Porch","3Ssn Porch","Screen Porch","Wood Deck SF"]].fillna(0).sum(axis=1)
        for n,s in {"HasGarage":"Garage Area","HasBasement":"Total Bsmt SF","HasFireplace":"Fireplaces","HasPool":"Pool Area"}.items(): X[n]=(X[s].fillna(0)>0).astype(int)
        X["QualLivArea"]=X["Overall Qual"]*X["Gr Liv Area"]
        return X
def validate_engineered_features(X):
    missing=[c for c in ENGINEERED_FEATURES if c not in X.columns]
    assert not missing,f"Missing engineered features: {missing}"
    for c in ["HouseAge","RemodAge","TotalSF","TotalBathrooms","TotalPorchSF","QualLivArea"]:
        v=X[c].dropna(); assert np.isfinite(v).all(),f"{c} contains non-finite values"; assert (v>=0).all(),f"{c} contains negative values"
    for c in ["HasGarage","HasBasement","HasFireplace","HasPool"]: assert set(X[c].dropna().unique()).issubset({0,1}),f"{c} is not binary"
    return True
def validate_feature_alignment(X_train,X_other):
    assert list(X_train.columns)==list(X_other.columns),"Feature columns/order do not match"
    return True
