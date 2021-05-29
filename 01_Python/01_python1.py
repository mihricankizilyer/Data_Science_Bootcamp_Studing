##############################################
# PYTHON PROGRAMMING FOR DATA SCIENCE
##############################################
# Print Types
# String Methods
# Input
# Data Structers (List, Dict, Tuple, Set)
# Functions
# Default Arguments / Parameters
# Return Functions

##############################################
# PRINT TYPES
##############################################

# print
print("hello ai era")
name = "Jane"
age = 35
print(name, age)

# %
"Name: %s" % name
"Name: %s, Age: %s" %(name, age)

# str.format()
"Name: {}, Age:{}".format(name,age)
person = {"name": "Jane", "age":35}
"Name: {}, Age: {}".format(person["name"], person["age"])

# fstring
F"Name: {name}, Age: {age}"

##############################################
# STRINGS METHODS
##############################################

name = "Mary"

# len
len(name)
len("Data Science Bootcamp")
len("123456789")

# upper() & lower()
"dsmlbc".upper()
"DSMLBC".lower()

# replace
dir("dsmlbc")
hi = "Hello AI Era"
hi.replace("l","p")
hi = hi.replace("p","l")

# split
"Hello AI Era".split()

#strip
" dsds".strip()
"dsdsdsds".strip("o")

# capitalize
# capitalizes the first letter
"dsml".capitalize()

# isdigit
# is it number? True or False
"dsml".isdigit() # False

# isascii
# test for character representable as ascii value
"dsml".isascii() # True

# isalnum
# alphanumeric (either alphabets or numbers)
"dsml".isalnum() # True
"dsml5".isalnum() # True
"52".isalnum() # True

# input
num = input()
type(num)
num * 2
# number/2 -> TypeError ( num=str )
int(num) / 3

num1 = int(input())
num2 = int(input())
num1 * num2

##############################################
# DATA STRUCTURES
##############################################

# Numbers (int, float, complex)
# String
# Boolean TRUE-FALSE
# List
# Dictionary
# Tuple
# Set

##############################################
# LIST
##############################################

# replaceable
# index operations can be done
# inclusive

age = [21, 35, 49]
names = ["John","Alis","Jane"]
age_names = [21, "John", "35", "Alis", 49, "Jane"]
age[1] = 24
names[2] = "Jordan"


# list methods
dir(age)
names.append("Sanda")
names.pop(0) # delete 0.index

##############################################
# DICTIONARY
##############################################

# replaceable
# unordered
# inclusive

dictionary = {"DS": "Data Science",
              "ML": "Machine Learning",
              "BC": "Bootcamp"}
len(dictionary)

dictionary = {"DS": 3,
              "ML": 5,
              "BC": 7}

dictionary = {"DS": ["Python", 3],
              "ML": ["R", 5],
              "BC": ["Scala",4]}
dictionary["DS"]
"DS" in dictionary

# Giving value according to key
dictionary["ML"]
dictionary.get("ML")

# Changing Value
dictionary ["ML"] = 44

# Access all key values
dictionary.keys()

# Access values
dictionary.values()

# Convert all pairs into tuples
dictionary.items()

# Updating key values
dictionary.update({"DS":38})

# Adding a new key value
dictionary.update({"MSSQL": 25})

# Deleting an item with a key
dictionary.pop("MSSQL")

##############################################
# TUPLE
##############################################

# unchangeable
# inclusive

a = ("Mary","Jane",28,33)
a[0:2]
# a[0] = "Miss" ->unchangeable

# if want to change!
a = list(a)
a[0] = 15
a = tuple(a)

##############################################
# SET
##############################################

# changeable
# Unordered
# Unique


# difference():
# The difference of the two sets
a = set([2,5,8])
b = set([3,6,9])

# Those in a but not in b.
a.difference(b)
# a - b

b.difference((a))
# b - a


# symmetric_difference()
# Not relative to each other in both clusters
a.symmetric_difference((b))


# intersection()
# The intersection of two sets
a = set([1,4,7])
b = set([1,5,8])
a.intersection((b))


# union()
# combination of two sets
a.union(b)

# isdisjoint()
# Is the intersection of two sets empty?
a = set([1,2,3,4,5,6])
b = set([5,3,6,2,5,8,9,4])
a.isdisjoint(b)


# issubset()
# Is one set a subset of the other?
a.issubset(b)

# issuperset()
# Does one cluster cover the other cluster?
b.issuperset(a)

##############################################
# FUNCTIONS
##############################################

print("DS","ML",sep = "&")

def programming():
    print("Python")
    print("R")
    print("C")
programming()

#func liste
rlist = []
def cal(a,b):
    rlist.append(a*b)
    print("Result: ",rlist)
cal(5,3)

# Docstring
# It is created for the document of the relevant function.
def cal(num1, num2):
    """
    The multiplication of two numbers
    args:
    -----
    :param num1: int, float
    :param num2: int, float
    :return:
    """
    print(num1 * num2)
help(cal)
cal(5,8)

# def function_name(parameters/arguments):
#      statements (function body)

##############################################
# DEFAULT ARGUMENTS/PARAMETERS
##############################################

def cal(x, y=8):
    print(x / y)
cal(2,2)

##############################################
# HOW DO YOU WRITE FUNCTIONS CORRECTLY?
##############################################

# PEP8
# DRY (don't repeat yourself)
# DoT (Do one Thing)
# modularity

##############################################
# WHEN DO WE NEED TO WRITE A FUNCTION?
##############################################

def cal(a, b, c):
    print((a + b) / c)
cal(20,30,40)

#######################
# Return
#######################

#Using Function Outputs as Inputs
# cal(20,30,40) * 10 # type error
type(cal(90,12,12))

def std(f,p):
    return f * 10 / 100 * p * p
std(10,9)

# Let's define a function that calls two functions.
# Our aim is to call cal and std functions.

def allf(a,b,c,f,p):
    x = cal(a,b,c)
    y = std(f,p)
    print(y*10)
allf(10,20,30,40,66)

#######################
# Local & Global Variables
#######################

rlist = [3,5]

def cal(x,y):
    z = x * y
    rlist.append(z)
    print(rlist)
cal(12,17)
