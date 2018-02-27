import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("Dataset/train.csv")

# Calculate Gain of "Education"
print("Confusion Matrix of Education")
print(df.groupby("Education").size())
print(df.groupby(["Education","Loan_Status"]).size())
