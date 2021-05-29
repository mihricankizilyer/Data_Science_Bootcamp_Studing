#############################################
# PANDAS
#############################################

# Panel Data: Two-dimensional concept that is watched over and over again
# It is an open source Python library written for data manipulation and data analysis.
# It provides the ability to read and write many different data types.

# Pandas Series
# Reading Data
# Quick Look at Data
# Selection in Pandas
# Aggregation & Grouping
# Apply & Lambda
# Join

#############################################
# Pandas Series
#############################################
import pandas as pd

s = pd.Series([14,25,36,47,58,69])
type(s)        # pandas.core.series.Series
s.index        # RangeIndex(start=0, stop=6, step=1)
s.dtype        # dtype('int64')
s.size         # 6
s.ndim         # 1
s.values       # array([14, 25, 36, 47, 58, 69], dtype=int64)
type(s.values) # numpy.ndarray
# If you're using values -> convert numpy array
s.head(2)      # first 2 number
s.tail(2)      # last 2 number

#############################################
# Reading Data
#############################################

import pandas as pd
df = pd.read_csv('datasets/titanic.csv')

#############################################
# Reading Multiple CSV Files in a Directory and Converting to a Single DF
#############################################

import glob
import pandas as pd
all_files = glob.glob(r'datasets/csv_path' + "/*.csv")
# "/*.csv" -> means those ending with csv
# "datasets/csv_path" -> the file containing all datasets

file_list = [pd.read_csv(f) for f in all_files]
# f -> each file
# thus all files can be read
# file_list = all csv files

all_df = pd.concat(file_list, axis=0, ignore_index=True)
# convert to dataframe
# pd.concat = It concat directly over headings or over indexes.

all_df = pd.concat(map(pd.read_csv, glob.glob('datasets/csv_path/*.csv')))
# short version

#############################################
# Quick Look at Data
#############################################

df = pd.read_csv('datasets/csv_path/titanic.csv')
df.shape   # Variable and number of observations
df.info()  # more detail
df.columns # names of variables of the data set # Index([...])
df.index   # RangeIndex(start=0, stop=891, step=1)

df.describe().T
# It allows us to quickly observe the summary statistics of the numerical variables in the data set.

df.isnull().values.any()
# number of missing values in data

df.isnull().sum()
# number of missing values in all variables

df["Sex"].value_counts()
# class number
# categorical variable analysis

#############################################
# Selection in Pandas
#############################################

# Transactions on Index
# Variable to Index
# Converting Index to Variable
# Operations on Variables
# Operations on Values
# iloc & loc
# Conditional Selection

#######################
# Transactions on the Index
#######################

df.index                   # RangeIndex(start=0, stop=891, step=1)
df[13:18]
df.drop(0,axis = 0).head() # 0.index deleted
delete_indexes = [1,3,5,7]
df.drop(delete_indexes, axis=0).head(10) # del index -> axis=0

# df.drop(delete_indexes, axis=0, inplace = True).head(10)
# to do the operation permanently -> index=True

#######################
# Converting the variable to Index
#######################

# Convert PassengerId to index
df.sort_values("PassengerId").head()
df = df.sort_values("PassengerId")
df.index = df["PassengerId"]
df.head()

# Delete Variables
df.drop("PassengerId", axis=1).head() # del category -> axis = 1

df.loc[:, df.columns != "PassengerId"].head()
# all rows # :
# All columns except Passenger Id # df.columns != "PassengerId"

df.drop("PassengerId", axis = 1, inplace = True)
df.index
# index name 0 'PassengerId'

#######################
# Converting the Index to a Variable
#######################

# df[x] -> # If a string expression(x) that is not in df is entered, it is to define a new variable.
df["PassengerId"] = df.index

df.reset_index().head()
# moves the index information from the row to the column

df = df.reset_index()
# saves permanently

#######################
# Operations on Variables
#######################

# return -> True or False
"Age" in df

# select variable from dataframe
df["Age"].head()

# converted to series because single square brackets are used
# function will not work
type(df["Age"]) # -> pandas.core.series.Series

# make it be dataframe
df[["Age"]].head()
type(df[["Age"]]) # ->  pandas.core.frame.DataFrame

# Select variable differently
df.Age.head()

# Choosing more than one variable
df[["Age","PassengerId"]].head()

# Choosing an element by the list
col_names = ["Age","Embarked","Ticket"]
df[col_names]

# Creating a new variable
df["Age2"] = df["Age"] ** 2
df["Age3"] = df["Age"] / df["Age2"]

# Deleting Variables
df.drop("Age2", axis = 1).head()

# Deleting an element with a list
col_names = ["Age","Embarked","Ticket"]
df.drop(col_names, axis = 1).head()

####
# If it contains age, delete it.
# Select if it does not contain age statement.
####
# '~' -> not
df.loc[:, ~df.columns.str.contains("Age")]
df.loc[:, df.columns.str.contains("Age")]

#######################
# Operations on Values
#######################

type(df.values) # -> numpy.ndarray
df.values

for row in df.values:
    print(row[1] + row[2])

#######################
# iloc & loc
#######################

# iloc: integer based selection
df.head()
df.iloc[0:3] # index = 0, 1, 2
df.iloc[0,0]

# loc: label based selection
df.loc[0:3] # index = 0, 1, 2, 3

# can be used like this in simple choices
df[0:3]

# df[0:3, "Age"] -> Type Error -> invalid key
# The index information here can only be kept with "loc".
# df.iloc[:3, "Age"] -> Value Error ->  just can be int value -> "Age" is string value
df.loc[0:3, "Age"]

col_names = "Age","Embarked","Ticket"
df.loc[0:3, col_names]

# If you want to choose only int base -> iloc
# When choosing a specific set of variables -> loc

#######################
# Conditional Selection
#######################

df["Age"].head()
df.Age.head()
df[["Age"]].head()

df["Age"] > 50             # return-> True or False
df[df["Age"] > 50]         # values that satisfy the condition
df[df["Age"] > 50].count() # the number of those greater than 50

df[df["Age"] > 50]["PassengerId"].count()

df[df["Age"] > 50]["Name"]

df[df["Age"] > 50]["Name"].nunique() # number of unique names

# One_conditional
df.loc[df["Age"] > 50, "Name"].head() # Fetch the variable and name value greater than 50

# Two_conditional
# if the condition is entered, it is entered in parentheses!
df[(df["Age"] > 50) & (df["Sex"] == "female")].head()
df[(df["Age"] > 50) & (df["Sex"] == "female")]["PassengerId"].count()

#############################################
# Aggregation & Grouping
#############################################

# count()
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum()
# pivot table

df[df["Age"] > 50][["PassengerId","Sex"]]

df.loc[df["Age"] > 50,["PassengerId","Sex"]].groupby("Sex").agg({"count"})

df.loc[df["Age"] > 50,["Age","Sex"]].groupby("Sex").agg(["mean","max"])

df.loc[df["Age"] > 50, ["PassengerId","Age","Sex"]].groupby("Sex").agg(["mean","max"])

df.loc[df["Age"] > 50, ["PassengerId","Age","Sex"]].groupby("Sex").agg({"PassengerId":"count","Age":"mean"})

df.loc[:,["PassengerId","Age","Sex"]].groupby("Sex").agg({"PassengerId":"count", "Age":["count","mean","sum"]})

# groupby["..","...","...."] -> makes the breakdown according to the data of the request
df.groupby(["Sex","Embarked","Pclass"]).agg({"PassengerId":"count", "Age":["count","mean","sum"]})

agg_funcitons = ["nunique","first","last","sum","var","std"]
df.groupby(["Sex","Embarked","Pclass"]).agg({"PassengerId":"count","Age": agg_funcitons})

#######################
# Pivot table
#######################

df = pd.read_csv('datasets/csv_path/titanic.csv')

def load_titanic():
    return pd.read_csv('datasets/csv_path/titanic.csv')
df = load_titanic()

df.pivot_table(values = "Age", index = "Sex", columns = "Embarked")
df.pivot_table(values = "Age", index = "Sex", columns = "Embarked", aggfunc = "std")

#######################
# Converting a Numerical Variable to a Categorical Variable
#######################

df.head()
# cut -> divides into specific parts according to given intervals
# qcut -> quantile cut -> divides by quarter values

df["new_age"] = pd.cut(df["Age"], [0,10,18,25,40,90])

df.pivot_table("Survived", index = "Sex", columns = "new_age")

df.pivot_table("Survived", index = ["Sex","Pclass"], columns = "new_age")

#############################################
# Apply ve Lambda
#############################################

# Apply: It provides the possibility to use functions in rows or columns.
# Lambda: It can be directly defined and used in relevant functions without any assignment.

(df["Age"] ** 2).head()

for col in df.columns:
    if "Age" in col:
        print(col)

for col in df.columns:
    if "Age" in col:
        print((df[col] ** 2).head())

for col in df.columns:
    if "Age" in col:
        df[col] = df[col] ** 2

df[["Age"]].apply(lambda x: x ** 2).head()

df.loc[:, df.columns.str.contains('Age')].apply(lambda x: x**2).head()

#1.way
# standardization function -> (x - x.mean()) / x.std())
df.loc[:, df.columns.str.contains('Age')].apply(lambda x : (x - x.mean()) / x.std()).head()

#2.way
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()
df.loc[:, df.columns.str.contains('Age')].apply(standart_scaler).head()

df.loc[:, ["Age","Age2","Age2"]] = df.loc[:, df.columns.str.contains('Age')].apply(standart_scaler)
# df.loc[:,..] -> selection process
# gets df permanently processed
df.head()

#############################################
# Join Operations
#############################################

import numpy as np
import pandas as pd

m = np.random.randint(1,30,size=(5,3))
df1 = pd.DataFrame(m, columns = ["var1","var2","var3"])
df2 = df1 + 99

#######################
# Concat
#######################

pd.concat([df1,df2], ignore_index = True)

# Change variable names
df2.columns = ["var1","var2","col3"]
df2.columns

# There are gaps in the converging df (NaN)
pd.concat([df1,df2])

# If you want to get only intersecting variables
pd.concat([df1,df2], join="inner")

#######################
# Merge
#######################

# Merge: combines by common intersecting variable
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

# Purpose: To reach the start date of each employee
pd.merge(df1,df2)
pd.merge(df1,df2, on="employees")

# Purpose: Accessing the information of each employee's manager
df3 = pd.merge(df1,df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['John', 'Pitty', 'Jessica']})

pd.merge(df3, df4)

# Purpose: Matching professional group skills with people
df5 = pd.DataFrame({'group': ['accounting', 'accounting', 'engineering', 'engineering', 'hr', 'hr'],
                    'skills': ['math', 'excel', 'coding', 'linux', 'excel', 'management']})

pd.merge(df1, df5)
