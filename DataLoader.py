import pandas as pd
import numpy as np

class DataLoader:
    def getDataSet():
        
        df=pd.read_csv("Dataset/train_new.csv")

        ''' Gender '''
        # X["balance"].fillna(df.balance.median(), inplace=True)
        GenderTypes = ["Male","Female"]
        df.Gender = df.Gender.astype("category",categories=GenderTypes).cat.codes
        # Through the visualization done above we can infer that belonging to any particular gender does not influence much the chances of getting a loan, hence we can remove this particular attribute.
        df=df.drop(['Gender'], axis=1)


        '''Married'''
        df=df.ix[~(df['Married'].isnull())]
        MarriedTypes = ["No","Yes"]
        df.Married = df.Married.astype("category",categories=MarriedTypes).cat.codes


        '''Education'''
        EducationTypes = ["Graduate","Not Graduate"]
        df.Education = df.Education.astype("category",categories=EducationTypes).cat.codes


        '''Self Employed'''
        df['Self_Employed']=df['Self_Employed'].fillna('No')
        Self_EmployedTypes = ["No","Yes"]
        df.Self_Employed = df.Self_Employed.astype("category",categories=Self_EmployedTypes).cat.codes


        '''Applicant Income'''
        df["ApplicantIncome"] = pd.qcut(df.ApplicantIncome, 5, labels=[0,1,2,3,4])


        '''Coapplicant Income'''
        df["CoapplicantIncome"] = pd.cut(df.CoapplicantIncome, 5, labels=[0,1,2,3,4])


        '''Loan Amount'''
        df["LoanAmount"].fillna(df.LoanAmount.median(), inplace=True)
        df["LoanAmount"] = pd.qcut(df.LoanAmount, 3, labels=[0,1,2])


        '''Loan Amount Term'''
        df["Loan_Amount_Term"].fillna(df.Loan_Amount_Term.median(), inplace=True)
        df["Loan_Amount_Term"] = pd.cut(df.Loan_Amount_Term, 3, labels=[0,1,2])


        '''Credit History'''
        df['Credit_History']=df['Credit_History'].fillna(0)
        df.Credit_History = df.Credit_History.astype(int)


        '''Property Area'''
        PropertyAreaTypes = ["Urban","Rural","Semiurban"]
        df.Property_Area = df.Property_Area.astype("category",categories=PropertyAreaTypes).cat.codes


        '''Loan Status'''
        Loan_StatusTypes = ["N","Y"]
        df.Loan_Status = df.Loan_Status.astype("category",categories=Loan_StatusTypes).cat.codes


        '''Dependents'''
        df["Dependents"].replace('3+',3,inplace=True)
        df["Dependents"].replace('0.0',0,inplace=True)        
        df["Dependents"].replace('0',0,inplace=True)        
        df["Dependents"].replace('1',1,inplace=True)        
        df["Dependents"].replace('2',2,inplace=True)        
        df["Dependents"].replace(0.0,0,inplace=True)        
        df["Dependents"].fillna(df.Dependents.median(), inplace=True)
        df.Dependents = df.Dependents.astype(int)


        Y = df["Loan_Status"]
        X = df.drop(['Loan_Status','Loan_ID'], axis=1)

        # pd.DataFrame.to_csv()
        df.to_csv("data.csv")


        # print(X)

        return X,Y,df



class TestDataLoader:
    def getDataSet():
        
        df=pd.read_csv("Dataset/test_new.csv")

        ''' Gender '''
        # X["balance"].fillna(df.balance.median(), inplace=True)
        GenderTypes = ["Male","Female"]
        df.Gender = df.Gender.astype("category",categories=GenderTypes).cat.codes
        # Through the visualization done above we can infer that belonging to any particular gender does not influence much the chances of getting a loan, hence we can remove this particular attribute.
        df=df.drop(['Gender'], axis=1)


        '''Married'''
        df=df.ix[~(df['Married'].isnull())]
        MarriedTypes = ["No","Yes"]
        df.Married = df.Married.astype("category",categories=MarriedTypes).cat.codes

        
        '''Dependents'''
        df["Dependents"].replace('3+','3',inplace=True)
        df["Dependents"].replace('0.0','0',inplace=True)        
        df["Dependents"].fillna(df.Dependents.median(), inplace=True)


        '''Education'''
        EducationTypes = ["Graduate","Not Graduate"]
        df.Education = df.Education.astype("category",categories=EducationTypes).cat.codes


        '''Self Employed'''
        df['Self_Employed']=df['Self_Employed'].fillna('No')
        Self_EmployedTypes = ["No","Yes"]
        df.Self_Employed = df.Self_Employed.astype("category",categories=Self_EmployedTypes).cat.codes


        '''Applicant Income'''
        df["ApplicantIncome"] = pd.qcut(df.ApplicantIncome, 5, labels=[0,1,2,3,4])


        '''Coapplicant Income'''
        df["CoapplicantIncome"] = pd.cut(df.CoapplicantIncome, 5, labels=[0,1,2,3,4])


        '''Loan Amount'''
        df["LoanAmount"].fillna(df.LoanAmount.median(), inplace=True)
        df["LoanAmount"] = pd.qcut(df.LoanAmount, 3, labels=[0,1,2])


        '''Loan Amount Term'''
        df["Loan_Amount_Term"].fillna(df.Loan_Amount_Term.median(), inplace=True)
        df["Loan_Amount_Term"] = pd.cut(df.Loan_Amount_Term, 3, labels=[0,1,2])


        '''Credit History'''
        df['Credit_History']=df['Credit_History'].fillna(0)


        '''Property Area'''
        PropertyAreaTypes = ["Urban","Rural","Semiurban"]
        df.Property_Area = df.Property_Area.astype("category",categories=PropertyAreaTypes).cat.codes


        '''Loan Status'''
        StatusTypes = ["N","Y"]
        df.Loan_Status = df.Loan_Status.astype("category",categories=StatusTypes).cat.codes


        Y = df["Loan_Status"]
        X = df.drop(['Loan_Status','Loan_ID'], axis=1)


        # print(X)

        return X,Y,df