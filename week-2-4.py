import scipy.stats as stats
import numpy as np
import pandas as pd

vac_data = pd.read_csv("../files/NISPUF17.csv")
cpox = vac_data[["HAD_CPOX","P_NUMVRC"]].dropna()
cpox = cpox.where(cpox["HAD_CPOX"] < 3).dropna()
#print(cpox)
corr, pval=stats.pearsonr(cpox["HAD_CPOX"],cpox["P_NUMVRC"])
print(corr)