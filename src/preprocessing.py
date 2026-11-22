"""Leakage-safe preprocessing utilities for Ames Housing."""
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder,StandardScaler
ORDINAL_CATEGORY_MAP={"Exter Qual":["Po","Fa","TA","Gd","Ex"],"Exter Cond":["Po","Fa","TA","Gd","Ex"],"Bsmt Qual":["None","Po","Fa","TA","Gd","Ex"],"Bsmt Cond":["None","Po","Fa","TA","Gd","Ex"],"Heating QC":["Po","Fa","TA","Gd","Ex"],"Kitchen Qual":["Po","Fa","TA","Gd","Ex"],"Fireplace Qu":["None","Po","Fa","TA","Gd","Ex"],"Garage Qual":["None","Po","Fa","TA","Gd","Ex"],"Garage Cond":["None","Po","Fa","TA","Gd","Ex"],"Pool QC":["None","Fa","TA","Gd","Ex"],"Bsmt Exposure":["None","No","Mn","Av","Gd"],"BsmtFin Type 1":["None","Unf","LwQ","Rec","BLQ","ALQ","GLQ"],"BsmtFin Type 2":["None","Unf","LwQ","Rec","BLQ","ALQ","GLQ"],"Functional":["Sal","Sev","Maj2","Maj1","Mod","Min2","Min1","Typ"],"Garage Finish":["None","Unf","RFn","Fin"],"Paved Drive":["N","P","Y"]}
def build_preprocessor(X,scale_numeric=False):
    num=X.select_dtypes(include=np.number).columns.tolist(); cat=X.select_dtypes(exclude=np.number).columns.tolist()
    ordc=[c for c in ORDINAL_CATEGORY_MAP if c in cat]; nom=[c for c in cat if c not in ordc]
    ns=[("imputer",SimpleImputer(strategy="median"))]
    if scale_numeric: ns.append(("scaler",StandardScaler()))
    return ColumnTransformer([("numeric",Pipeline(ns),num),("ordinal",Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("ordinal",OrdinalEncoder(categories=[ORDINAL_CATEGORY_MAP[c] for c in ordc],handle_unknown="use_encoded_value",unknown_value=-1))]),ordc),("nominal",Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]),nom)])
