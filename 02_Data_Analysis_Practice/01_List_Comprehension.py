
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


# Task 1: Convert the names of numeric variables in the car_crashes data to uppercase letters and add NUM in front of them.
["NUM"+col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns ]


# Task 2: Write "FLAG" AT the END of the variables that do NOT contain "no" in their name.
[col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]


# Task 3: Create a new df by selecting the names of the variables that are DIFFERENT from the variable names given below.
og_list = ["abbrev","no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()
