import pandas as pd

vac_data = pd.read_csv("../files/NISPUF17.csv")
mom_edu = vac_data["EDUC1"]
print(mom_edu.size)
print(mom_edu.value_counts()[1])
print(mom_edu.value_counts()[2])
print(mom_edu.value_counts()[3])
print(mom_edu.value_counts()[4])
print(mom_edu.value_counts()[1]/mom_edu.size)
dict = {"less than high school":mom_edu.value_counts()[1]/mom_edu.size,
        "high school":mom_edu.value_counts()[2]/mom_edu.size,
        "more than high school but not college":mom_edu.value_counts()[3]/mom_edu.size,
        "college":mom_edu.value_counts()[4]/mom_edu.size}
print(dict)