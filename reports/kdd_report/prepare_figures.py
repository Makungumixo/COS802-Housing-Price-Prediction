from pathlib import Path
import json, base64
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
E=ROOT/'evidence'
F=ROOT/'figures'
F.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'pdf.fonttype':42,'axes.spines.top':False,'axes.spines.right':False})
d=pd.read_csv(E/'approved_model_family_comparison.csv')
fig,ax=plt.subplots(figsize=(3.35,2.3))
order=['Linear Regression','Ridge','Random Forest','XGBoost']
for i,m in enumerate(order):
    z=d[d.Model==m].set_index('Representation')
    a,b=z.loc['Original','RMSE_mean']/1000,z.loc['Engineered','RMSE_mean']/1000
    ax.plot([a,b],[i,i],color='0.6',zorder=1)
    ax.scatter(a,i,color='#555555',marker='o',label='Original' if i==0 else None)
    ax.scatter(b,i,color='#17658a',marker='s',label='Engineered' if i==0 else None)
ax.set_yticks(range(4),['Linear','Ridge','Random forest','XGBoost']); ax.invert_yaxis()
ax.set_xlabel('Development CV RMSE (USD 1,000)')
ax.set_xlim(20,34); ax.legend(frameon=False,fontsize=8,loc='lower right')
fig.tight_layout(); fig.savefig(F/'cv_comparison.pdf'); plt.close(fig)
d=pd.read_csv(E/'shap_global_importance.csv').head(8).iloc[::-1]
fig,ax=plt.subplots(figsize=(3.35,2.6))
ax.barh(d.Feature,d.MeanAbsSHAP/1000,color='#17658a')
ax.set_xlabel('Mean absolute SHAP (USD thousands)')
fig.tight_layout(); fig.savefig(F/'shap_importance.pdf'); plt.close(fig)
nb=json.loads((E/'notebook05.ipynb').read_text(encoding='utf-8-sig'))
for cell in nb['cells']:
    src=''.join(cell.get('source',[]))
    if 'final_residuals_vs_predicted.png' in src:
        ims=[o['data']['image/png'] for o in cell.get('outputs',[]) if 'image/png' in o.get('data',{})]
        if ims: (F/'residuals.png').write_bytes(base64.b64decode(ims[0]))
print('Figure files:',[p.name for p in F.iterdir()])
