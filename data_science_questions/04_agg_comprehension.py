#######################
# Purpose: To dynamically format each element of the list in the Value section.
#######################

# before:
# {'total': ['mean', 'min', 'max', 'sum'],
#  'speeding': ['mean', 'min', 'max', 'sum'],
#  'alcohol': ['mean', 'min', 'max', 'sum']}

# after:
# {'total': ['total_mean', 'total_min', 'total_max', 'total_var'],
#  'speeding': ['speeding_mean', 'speeding_min', 'speeding_max', 'speeding_var'],
#  'alcohol': ['alcohol_mean', 'alcohol_min', 'alcohol_max', 'alcohol_var']}


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype !="O"]
agg_list = ["mean","min","max","sum"]

{col: [str(col) + "_" + c for c in agg_list] for col in num_cols}
