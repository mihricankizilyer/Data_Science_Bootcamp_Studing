#############################################
# WEEK_2 -> HOMEWORK 2: DOCSTRİNG
#############################################
# Write a numpy-style docstring containing 4 information (if appropriate) to the functions below.
# (task, params, return, example)
# check_df(), cat_summary()

def check_df(dataframe, head = 5):
    """
    Task
    ---
    Task will give information about:
    - shape: number of elements per axis
    - types: array data type
    - head: first n observations
    - tail: last n observations
    - NA: null value
    - Quantiles: divides by the specified range values
    in the dataset.

    Parameters
    ----------
    dataframe: DataFrame
            Dataframe to get variable names
    head: int, optional
            first n observation

    Exapmle:
    ----------
            df = pd.read_csv("datasets/csv_path/titanic.csv")
            check_df(df, 10)
    """
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
check_df(df)

def cat_summary(dataframe, col_name, plot = False):
    """
    Parameters
    ----------
    dataframe: DataFrame
            Dataframe to get variable names
    col_name: string
            Name of the column to be analyzed in the dataframe
    Example
    ----------
    df = pd.read_csv("datasets/csv_path/titanic.csv")
    cat_summary(df, "Sex", plot = True)
    """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("******************")
    if plot:
        sns.countplot(x = dataframe[col_name], data = dataframe)
        plt.show()
cat_summary(df, "Sex", plot = True)