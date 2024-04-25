import csv
import os
import numpy as np
import pandas as pd

def make_df(path): # Reads the csv file in and makes it a DataFrame
    df = pd.read_csv(path)
    return df

ordinal = []

path = os.path.realpath(__file__)                       #| This is here just so we can avoid 
directory = os.path.dirname(path)                       #| file directory headaches
dir_string = str(directory) + "/data/crime_data.csv"    #| in the future.

all_data_df = make_df(dir_string)

# print(list(all_data_df)) #This line spits out all of the categories from the main dataset (the column titles)

date_crime = pd.concat([all_data_df['Occurred Date'], all_data_df['Highest Offense Description']], axis=1)

# print(date_crime.sort_values(by=['Highest Offense Description']))
crimes = date_crime['Highest Offense Description'].unique() #This populates a list containing the different types of crimes

# print(crimes)

# print(date_crime)

filtered_theft_crime = date_crime[date_crime['Highest Offense Description'].str.contains('theft', case=False)]
filtered_burgl_crime = date_crime[date_crime['Highest Offense Description'].str.contains('burglary', case=False)]

all_theft_crimes = pd.concat([filtered_theft_crime, filtered_burgl_crime], ignore_index=True)

bins = [pd.Timestamp(year, month, 20) for year in range(2003, 2024) for month in [3, 6, 9, 12]]

all_theft_crimes['Occurred Date'] = pd.to_datetime(all_theft_crimes['Occurred Date'], format='mixed')

all_theft_crimes['Season'] = pd.cut(
    all_theft_crimes['Occurred Date'].dt.dayofyear,
    bins= [31, 91, 152, 212, 365],
    labels=['Winter', 'Spring', 'Summer', 'Fall']
    )

print(all_theft_crimes)