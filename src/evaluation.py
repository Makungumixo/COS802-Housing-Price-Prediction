"""Regression evaluation and bootstrap uncertainty utilities."""
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
def regression_metrics(y_true,y_pred):
    return {"MAE":mean_absolute_error(y_true,y_pred),"RMSE":np.sqrt(mean_squared_error(y_true,y_pred)),"R2":r2_score(y_true,y_pred)}
def bootstrap_metric_intervals(y_true,y_pred,n_boot=5000,seed=16153970,alpha=.05):
    y_true=np.asarray(y_true); y_pred=np.asarray(y_pred); rng=np.random.default_rng(seed); n=len(y_true); rows=[]
    for _ in range(n_boot):
        idx=rng.integers(0,n,n); rows.append(regression_metrics(y_true[idx],y_pred[idx]))
    b=pd.DataFrame(rows); point=regression_metrics(y_true,y_pred); out=[]
    for m in ["MAE","RMSE","R2"]:
        lo,hi=b[m].quantile([alpha/2,1-alpha/2]); out.append({"Metric":m,"Estimate":point[m],"CI_Lower":lo,"CI_Upper":hi})
    return pd.DataFrame(out)
