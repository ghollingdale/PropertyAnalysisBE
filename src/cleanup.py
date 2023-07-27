# Import modules
import numpy as np
import pandas as pd

# Read uncleaned csv
def read_raw_csv(filepath='..\data\properties.csv'):
    df = pd.read_csv(filepath, header=0)
    return df

# Read clean csv  
def read_clean_csv(filepath='..\data\cleaned_output.csv'):
    df = input("Enter name of dataframe.")
    df = pd.read_csv(filepath, header=0)
    return df

# Read shape of the properties dataframe  
def df_properties(df):
    shape = df.shape
    return print("The data set consists of " + str(shape[0]) + " rows and " + str(shape[1]) + " columns.")

# Check distribution of unique values in each column
def unique_df_values(df):
    for column in df.columns:
        column_data = df[column]
        value_counts = column_data.value_counts()
    return print(value_counts , '\n')

# Confirm there are no duplicated rows using 'id' column as default
def check_duplicates(df, key='id'):
    duplicates = df[key].duplicated().any()
    if duplicates:
        return print("Some rows are duplicated")
    else:
        return print("Every row is unique")
    
def replace_spaces_with_underscores(df):
    new_column_names = [col.replace(' ', '_') for col in df.columns]
    df.columns = new_column_names
    return df
    
# Iterate through rows, then columns and replace booleans with binary
def replace_boolean(df):
    for ind , row in df.iterrows():
        for column in df.columns:   
            if row[column] == False:
                df.at[ind , column] = 0
            elif row[column] == True:
                df.at[ind , column] = 1
    return df

# Fill NaNs in a given column with a value
def replace_nan(df, column, value=0):
    try:
        df[column].fillna(value, inplace=True)
    except:
        pass
    return df

# Delete a column from df
def drop_column(df, column):
    try:
        df = df.drop(columns=column)
    except:
        pass
    return df


# Replace specific value in a given column with new_value
def replace_col_value(df, column, value, new_value):
    for index, row in df.iterrows():
        if row[column] == value:
            df.at[index, column] = new_value
    return df

# Swap the position of column_1 with column_2
def swap_columns_pos(df, column_1, column_2):
    columns = df.columns.tolist()
    columns[column_1] , columns[column_2] = columns[column_2] , columns[column_1]
    df = df[columns]
    return df

# Sorts the dataframe by the given column. Takes price column as default
def sort_by_column(df, column='price'):
    df = df.sort_values(by=column)
    return df

# Turn column types to floats where possible
def column_type_float(df):
    try:
        for column in df.columns:
            df[column] = df[column].astype("float")
    except:
        pass
    return df

# Check whether a value in one column exists, and whether the respective value in another coulmn doesn't exist. 
# If both are satisfied, replace the value in the second column with a given value
# E.g. if there exists a terrace area, but terrace doesn't have a value, give terrace a value
def check_for_adjascent_data(df, check_column, replacement_column, replacement_value):
    for index, row in df.iterrows():
        if row[check_column] != np.nan and row[replacement_column] == np.nan:
            df.at[index, replacement_column] = replacement_value
        return df
    
# Print the number of datapoints with a key maxvalue greater than maxvalue, then return the dataframe without those datapoints
def clean_greater_outliers(df, key, maxvalue):
    removal_count = 0 
    print(
        "There were", 
        df[df[key] > maxvalue].shape[0], 
        "properties with a", 
        str(key), 
        "value of more than", 
        maxvalue,
        "that have been removed."
        )
    removal_count = removal_count + df[df[key] > maxvalue].shape[0]
    df = df[df[key] <= maxvalue]
    return df

# Print the number of datapoints with a key maxvalue greater than maxvalue, then return the dataframe without those datapoints
def clean_lesser_outliers(df, key, maxvalue):
    removal_count = 0 
    print(
        "There were",
        df[df[key] < maxvalue].shape[0], 
        "properties with a", 
        str(key), 
        " value of less than", 
        maxvalue,"that have been removed."
        )
    removal_count = removal_count + df[df[key] < maxvalue].shape[0]
    df = df[df[key] >= maxvalue]
    return df

# Function to clean outliers
def clean_outliers(houses):
    houses = clean_greater_outliers(houses, 'price', 2000000)
    houses = clean_greater_outliers(houses, 'number_of_bedrooms', 10)
    houses = clean_greater_outliers(houses, 'living_area', 100)
    houses = clean_greater_outliers(houses, 'total_property_area', 750)
    houses = clean_greater_outliers(houses, 'total_land_area', 20000)
    houses = clean_greater_outliers(houses, 'terrace_area', 250)
    houses = clean_greater_outliers(houses, 'number_of_facades', 4)
    return houses