import pandas as pd
import numpy as np
from DataLoader import DataLoader
from DataLoader import TestDataLoader
from sklearn import tree

'''Load the Dataset'''
[X,Y,df] = DataLoader.getDataSet()

'''Classify using the scikit Decision Tree Classifier'''
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

'''Feed the test input'''
test = [1,1,0,0,3,0,1,2,1,1]
test = np.array(test).reshape((1,-1))


'''Predict the answer'''
result = clf.predict(test)
# if result == 0 :
    # print("Loan CAN NOT be granted")
# else :
    # print("Loan CAN be granted")


'''Load the test dataset'''
[X_test,Y_test,test_df] = TestDataLoader.getDataSet()
clf = clf.predict(X_test)
# print(Y_test)
# print(clf)
cnt = 0
for i in range(len(clf)):
    if clf[i] == Y_test[i]:
        cnt += 1
print("Accuracy = "+str((cnt/len(clf))*100))