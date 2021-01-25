import pandas as pd

df = pd.read_csv("chickens.csv")

# check out what we have
print(df.head())
print()

# see the data types we are working with
print(df.dtypes)
print()


# select a column by column name
# print(df["species"])

# changing the data type of a column
# df["sepal_length"] = df["sepal_length"].apply(int)
# print(df.dtypes)

# get row by index
# print(df.iloc[0])

first_row = df.iloc[0]  # selecting a row creates a pandas series that can be indexed like a column
# print(type(first_row[-1]))
# print()

# assuming the last column is our "target" or category we can check the amount and balance of our data
from utils import print_out_balance_info
# print_out_balance_info(dataframe=df)

# get column names
column_names = df.columns
# print(column_names)

# checkout the min and max of int and float columns
# for name in column_names:
#     single_column = df[name]
    
#     # pass over column if it contains strings
#     if isinstance(single_column[0], str):
#         continue

#     print(f"name: {name}")
#     print(f"length: {len(single_column)}")
#     min_val = min(single_column)
#     max_val = max(single_column)
#     print(f"min: {min_val}")
#     print(f"max: {max_val}")
#     print("-"*40)
    

# iterate across column names and iterate down column values
for col_index, name in enumerate(column_names):
    for row_index, value in enumerate(df[name]):
        print(df.iloc[row_index, col_index])
        # logic and reassignment here
        break
    break

