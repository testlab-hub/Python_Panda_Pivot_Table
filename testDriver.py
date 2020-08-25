import pandas as pd
import numpy as np

df = pd.read_excel("sales-funnel.xlsx")
console_1 = df.head()
# print(console_1)

# define the status column as a category
df["Status"] = df["Status"].astype("category")
df["Status"].cat.set_categories(["won", "pending", "presented", "declined"], inplace=True)

"""
Pivot the data -
The simplest pivot table must have a dataframe and an index . 
In this case, let’s use the Name as our index.
"""
console_2 = pd.pivot_table(df, index=["Name"])
# print(console_2)

# You can have multiple indexes, most of the pivot_table args can take multiple values via a list.
console_3 = pd.pivot_table(df, index=["Name", "Rep", "Manager"])
# print(console_3)

#  look at the table by Manager and Rep
console_4 = pd.pivot_table(df, index=["Manager", "Rep"])
# print(console_4)

# define the columns you need using the values field
using_values = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"])
# print(using_values)

# The price column automatically averages the data but we can do a count or a sum.
using_sum = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], aggfunc=np.sum)
# print(using_sum)

#  try a mean using the numpy mean function and len to get a count.
mean_len = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], aggfunc=[np.mean, len])
# print(mean_len)
"""
Columns vs. Values
==================
one of the confusing points with the pivot_table is the use of columns and values . 
Remember, columns are optional - they provide an additional way to segment the actual values you care about. 
The aggregation functions are applied to the values you list.
"""
nan_value = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"],
                           columns=["Product"], aggfunc=[np.sum])
# print(nan_value)

# removing NaN values with fill_value
remove_nan = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"],
                            columns=["Product"], aggfunc=[np.sum], fill_value=0)
# print(remove_nan)

quantity = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price", "Quantity"],
                          columns=["Product"], aggfunc=[np.sum], fill_value=0)
# print(quantity)
change_index = pd.pivot_table(df, index=["Manager", "Rep", "Product"],
                              values=["Price", "Quantity"], aggfunc=[np.sum], fill_value=0)
# print(change_index)

# use margins=True to get total
check_for_total = pd.pivot_table(df, index=["Manager", "Rep", "Product"],
                                 values=["Price", "Quantity"],
                                 aggfunc=[np.sum, np.mean], fill_value=0, margins=True)
# print(check_for_total)

analysis = pd.pivot_table(df, index=["Manager", "Status"], values=["Price"],
                          aggfunc=[np.sum], fill_value=0, margins=True)
# print(analysis)

# pass a dictionary
pass_dictionary = pd.pivot_table(df, index=["Manager", "Status"], columns=["Product"], values=["Quantity", "Price"],
                                 aggfunc={"Quantity": len, "Price": np.sum}, fill_value=0)
# print(pass_dictionary)

# You can provide a list of agg functions to apply to each value too
table = pd.pivot_table(df, index=["Manager", "Status"], columns=["Product"], values=["Quantity", "Price"],
                       aggfunc={"Quantity": len, "Price": [np.sum, np.mean]}, fill_value=0)
# print(table)
"""
Advanced Pivot Table Filtering
==============================
Once you have generated your data, it is in a DataFrame so 
you can filter on it using your standard DataFrame functions.
"""
example_1 = table.query('Manager == ["Debra Henley"]')
example_2 = table.query('Status == ["pending","won"]')
print(example_1, '\n', example_2)
