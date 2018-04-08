import pandas as pd
import numpy as np
from math import log
from DataLoader import DataLoader


'''Load Dataset'''
[X,y,df] = DataLoader.getDataSet()


'''Calculate the Info of the whole Dataset'''
m_dataset = df.groupby("Loan_Status").size()
no_dataset = m_dataset[0]
yes_dataset = m_dataset[1]
total_dataset = yes_dataset+no_dataset
no_ratio_dataset = no_dataset/total_dataset
yes_ratio_dataset = yes_dataset/total_dataset
info_dataset = -((no_ratio_dataset*log(no_ratio_dataset,2))+(yes_ratio_dataset*log(yes_ratio_dataset,2)))
print("Info of Dataset = "+str(info_dataset))


'''Calculate the Info of Married'''
m_married = df.groupby(["Married","Loan_Status"]).size()

no_no_married_ratio = m_married[0][0]/(m_married[0][0]+m_married[0][1])
no_yes_married_ratio = m_married[0][1]/(m_married[0][0]+m_married[0][1])
no_married_ratio = -((no_no_married_ratio*log(no_no_married_ratio))+(no_yes_married_ratio*log(no_yes_married_ratio)))

yes_no_married_ratio = m_married[1][0]/(m_married[1][0]+m_married[1][1])
yes_yes_married_ratio = m_married[1][1]/(m_married[1][0]+m_married[1][1])
yes_married_ratio = -((yes_no_married_ratio*log(yes_no_married_ratio))+(yes_yes_married_ratio*log(yes_yes_married_ratio)))

info_married = (((m_married[0][0]+m_married[0][1])/(m_married[0][0]+m_married[0][1]+m_married[1][0]+m_married[1][1]))*no_married_ratio+
    ((m_married[1][0]+m_married[1][1])/(m_married[0][0]+m_married[0][1]+m_married[1][0]+m_married[1][1]))*yes_married_ratio
)
gain_married = info_dataset - info_married
print("Gain of Married = "+str(gain_married))


'''Calculate the Gain of Dependents'''
m_dependents = df.groupby(["Dependents","Loan_Status"]).size()
print(m_dependents)
for i in range(5):
    print(m_dependents[2*i], m_dependents[(2*i)+1])
# no_no_dependents_ratio = m_dependents[0][0]/(m_dependents[0][0]+m_dependents[0][1])
# no_yes_dependents_ratio = m_dependents[0][1]/(m_dependents[0][0]+m_dependents[0][1])
# no_dependents_ratio = -((no_no_dependents_ratio*log(no_no_dependents_ratio))+(no_yes_dependents_ratio*log(no_yes_dependents_ratio)))

# yes_no_dependents_ratio = m_dependents[1][0]/(m_dependents[1][0]+m_dependents[1][1])
# yes_yes_dependents_ratio = m_dependents[1][1]/(m_dependents[1][0]+m_dependents[1][1])
# yes_dependents_ratio = -((yes_no_dependents_ratio*log(yes_no_dependents_ratio))+(yes_yes_dependents_ratio*log(yes_yes_dependents_ratio)))

# info_dependents = (((m_dependents[0][0]+m_dependents[0][1])/(m_dependents[0][0]+m_dependents[0][1]+m_dependents[1][0]+m_dependents[1][1]))*no_dependents_ratio+
#     ((m_dependents[1][0]+m_dependents[1][1])/(m_dependents[0][0]+m_dependents[0][1]+m_dependents[1][0]+m_dependents[1][1]))*yes_dependents_ratio
# )
# gain_dependents = info_dataset - info_dependents
# print("Gain of Dependents = "+str(gain_dependents))

# Calculate Gain of "Education"
# asd = X.groupby("Education").size()
# print(asd[0])
# abc = df.groupby(["Education","Loan_Status"]).size()
# print(abc[0][0])
