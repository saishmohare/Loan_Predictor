import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from DataLoader import DataLoader, TestDataLoader


df_train = pd.read_csv("Dataset/train.csv")
df_test = pd.read_csv("Dataset/test.csv")

# df_train = DataLoader.getDataSet()
df_train = df_train[["ApplicantIncome","LoanAmount"]]
df_train.dropna(axis=0,inplace=True)
df_train.columns = ['X','Y']
# print(df_train)

df_test = df_test[["ApplicantIncome","LoanAmount"]]
df_test.dropna(axis=0,inplace=True)
df_test.columns = ['X','Y']
# print(df_test)


'''Finding mean and variance of both colmns'''
mean_X = df_train["X"].mean()
mean_Y = df_train["Y"].mean()
variance_X = df_train["X"].var()
variance_Y = df_train["Y"].var()

'''Find the covariance between the two columns'''
covariance = df_train.cov()["X"]["Y"]

'''Calculate the values of coefficients'''
numer=0
denom=0
# dfX_t = np.asarray(df_train["X"])
# for i in range(0,len(df_train)):
    # print(df_train["X"][i],df_train["Y"][i])
    # numer += (df_train["X"][i] - mean_X) * (df_train["Y"][i] - mean_Y)
    # denom += (df_train["X"][i] - mean_X) ** 2
    # print(denom)
    
# print(dfX_t.var())
print(variance_X)
print(covariance)
print(mean_Y,mean_X)
b1 = covariance/variance_X
b0 = mean_Y - b1*mean_X


predicted_Y = []

for i in df_test["X"]:
    predicted_Y.append(b0+b1*i)

print(predicted_Y)
# print(y_test)
# # print(df_test["Y"].as_matrix(),np.asarray(predicted_Y))
# # print(mean_squared_error(df_test["Y"].as_matrix(),np.asarray(predicted_Y)))
# print(df_test["Y"], predicted_Y)
# x = np.linspace(0,100)
# y = b0 + b1 * x
# plt.plot(x, y, color='#58b970', label='Regression Line')
plt.plot(df_test["X"], df_test["Y"], 'ro',df_test["X"], predicted_Y, 'g^')
plt.show()