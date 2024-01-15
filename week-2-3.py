import pandas as pd

vac_data = pd.read_csv("../files/NISPUF17.csv")
cpox = vac_data[["SEX","HAD_CPOX","P_NUMVRC"]].dropna()
cpox = cpox.where(cpox["P_NUMVRC"] > 0).dropna()
hadcpox = cpox.where(cpox["HAD_CPOX"] == 1).dropna()
didnthadcpox = cpox.where(cpox["HAD_CPOX"] == 2).dropna()
#print(didnthadcpox.head())
mratio = hadcpox.where(hadcpox["SEX"] == 1).dropna().size/ didnthadcpox.where(didnthadcpox["SEX"] == 1).dropna().size
fratio = hadcpox.where(hadcpox["SEX"] == 2).dropna().size/ didnthadcpox.where(didnthadcpox["SEX"] == 2).dropna().size
ratio = {"male":mratio,"female":fratio}
print(ratio)