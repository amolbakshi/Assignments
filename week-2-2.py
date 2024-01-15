import pandas as pd
import numpy as np
vac_data = pd.read_csv("../files/NISPUF17.csv")
bfed_influ = vac_data[["CBF_01","P_NUMFLU"]].dropna()
bfed_kids = bfed_influ.where(bfed_influ["CBF_01"] == 1).dropna()
notbfed_kids = bfed_influ.where(bfed_influ["CBF_01"] == 2).dropna()
print(bfed_kids["P_NUMFLU"].sum())
flu1=bfed_kids['P_NUMFLU'].values.copy()
flu1[np.isnan(flu1)] = 0
f1=np.sum(flu1)/len(flu1)
#print(bfed_kids["P_NUMFLU"].size)
bfedAvg=bfed_kids["P_NUMFLU"].sum()/len(bfed_kids.index)
unbfedAvg=notbfed_kids["P_NUMFLU"].sum()/len(bfed_kids.index)
mytuple=(bfedAvg,unbfedAvg)
flu2=notbfed_kids['P_NUMFLU'].values.copy()
flu2[np.isnan(flu2)] = 0
f2=np.sum(flu2)/len(flu2)
print(mytuple)
aid=(f1,f2)
