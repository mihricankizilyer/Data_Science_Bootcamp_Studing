###############################################
# LOOPS
###############################################

tips = [200,350,460,179,330,647]
def cal(total, rate=20):
    return int(total * rate / 100 +total)
cal(100,15)

for tip in tips:
    print(cal(tip))

#break
for tip in tips:
    if tip == 330:
        print("break point")
        break
    print(tip)

# continue
# when a condition is met, the object in the iteration is discarded
for tip in tips:
    if tip == 460:
        continue
    print(tip)

# while
num = 1
while num < 20:
    print(num)
    num += 5

#######################
# Enumerate: For loop with automatic Counter / Indexer
#######################

# Problem:Dividing the employees in the list into 2 groups according to their index order
employees = ["Mary","Jane","Jessi","Ella","Tom","Jordan"]
for index, employee in enumerate(employees):
    print(index, employee)

X = []
Y = []
for index, employee in enumerate(employees):
    if index % 2 == 0:
        X.append(employee)
    else:
        Y.append(employee)
print(X, Y)

#######################
# Using Enumerate with a Specific Index
#######################

for index, employee in enumerate(employees, 2):
    print(index,employee)

#######################
# Zip
#######################

names = ["Mary","Jane","Jessi","Ella"]
ages = [24,33,15,42]
id = [1,2,3,4,]
print(list(zip(names,ages,id)))

###############################################
# lambda, map, filter, reduce
###############################################

def cal(a,b):
    return a-b
cal(7,5) * 9

# Lambda
calculate = lambda a,b: a*b

# Map
tips = [200,350,460,179,330,647]
def cal(x):
    return x*30/100+x
for tip in tips:
    print(cal(tip))

list(map(cal, tips))
list(map(lambda x: x * 20 / 100 + x, tips))
list(map(lambda x: x**2, tips))
list(map(lambda x: x.upper(), "dsmlbs"))

# Filter
num = [1,3,5,7,9,33,68,74]
list(filter(lambda x: x % 2 == 0, num))

# Reduce
from functools import reduce
num = [1,3,5,7,96,4,12,55]
reduce(lambda a,b: a + b, num)

###############################################
# COMPREHENSIONS
###############################################
def summer(a):
    return a**2
def multi(x):
    return x*3
#######################
# List Comprehension
#######################

tips = [350,664,874,214,365,235]

# for is on the far right
[tip**2 if tip<300 else tip / 2 for tip in tips]
[summer(tip*2) if tip > 300 else multi(tip/2) for tip in tips]

# If only "if" is used, "if" will be on the far right
[tip*3 for tip in tips if tip<300]

employess = ["Elly","Jhon","Mark","Jordan","Jane","Mary"]
lazy = ["Jordan","Jane"]

[employee.lower() if employee in lazy else employee.upper() for employee in employess]

# Meta information = Data types in the dataframe

#######################
# Dictionary Comprehension
#######################

dictionary = {'x':2, 'y':4, 'z':6, 'd':8}
dictionary["x"]
dictionary.keys()
dictionary.values()
dictionary.items()

for value in dictionary.values():
    print(value+3)

{k: v**2 for (k,v) in dictionary.items()}
{k.upper(): v for (k,v) in dictionary.items()}

#######################
# Purpose: Changing a Variable Name in a Data Set
#######################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
A = []
for col in df.columns:
    A.append(col.upper())
df.columns = A

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

#######################
# Add "FLAG" to the beginning of variables named "INS" and "NO FLAG" to others
#######################

df.columns
["FLAG_" + col for col in df.columns if "ins" in col]

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns = ["FLAG_" + col if "ins" in col else "NO_FLAG_" + col for col in df.columns]

#######################
# Writing CAT at the beginning of categorical variables
#######################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col for col in df.columns if df[col].dtype == "O"]
["CAT_" + col.upper() if df[col].dtype == "O" else col.upper() for col in df.columns]

#######################
# The aim is to create a word whose key string is a list as below.
#######################
# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

num_cols = [col for col in df.columns if df[col].dtype != "O"]
dict = {}
agg_list = ["mean","min","max","sum"]

for col in num_cols:
    dict[col] = agg_list

{ col : agg_list for col in num_cols}


# Practice
new_dict = { col : agg_list for col in num_cols}
df.groupby("abbrev").agg(new_dict)


# Practice 2
df = sns.load_dataset("tips")
num_cols = [col for col in df.columns if df[col].dtype in [int, float]]
new_dict = {col: agg_list for col in num_cols}

df.head
df.groupby("time").agg(new_dict)

