#############################################
# HOMEWORK 1: Adding Features to Functions.
#############################################

# Task: Add attribute to cat_summary() function. Let this property be formatted with arguments.
# Note: You can also make existing property controllable from the argument.
# What does it mean to add a feature to the function that can be formatted with an argument?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('datasets/csv_path/titanic.csv')


# BEFORE

def cat_summary(dataframe, col_name, plot = False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("******************")
    if plot:
        sns.countplot(x = dataframe[col_name], data = dataframe)
        plt.show()
        
cat_summary(df, "Age", plot = True)


# AFTER

def cat_summary(dataframe, col_name, plot = False, head = 5, cat_visualization = False, unique = False):
    if cat_visualization :
        if plot:
            sns.countplot(x = dataframe[col_name], data=dataframe)
            plt.show()
    else:
        print(pd.DataFrame(
            {col_name: dataframe[col_name].value_counts(),
             "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("######### Head #########")
        print(dataframe.head(head))
        if df[col_name].unique():
            print("######### Categorical Variable Values #########")
            print(f"Class and frequency:{df[col_name].value_counts()}")
            print(f"Variable classes:{df[col_name].unique()}")
            print(f"Unique number of classes: {df[col_name].nunique()}")
            
cat_summary(df,"Sex",plot = True)

cat_summary(df, "Age", plot = True, head = 10, cat_visualization = True, unique = True )
