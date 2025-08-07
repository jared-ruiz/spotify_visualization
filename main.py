import pandas as pd
import numpy as np
import json

# acquire json title
data_file = input("Please provide your data file for utilization: ")

# handle quick user input
if len(data_file) < 3:
    try:
        with open('./json_data/StreamingHistory_music_0.json', 'r', encoding='utf-8') as file:
            init_data = json.load(file)

            
            df = pd.DataFrame(init_data)
            # print(df)
            
    except:
        print('file name not detected.')
 
# Adjust dataframe columns
df = df.rename(columns={
     'endTime': 'End_Time',
     'artistName': 'Artist',
     'trackName': 'Track',
     'msPlayed': 'Seconds_Played'
     })

# print(df)

# Convert MS Within Seconds_Played to Seconds (Divide ms value by 1000)
df['Seconds_Played'] = (df['Seconds_Played'] / 1000).round(2)
# print(df)

# Change End_Time type from object to datetime object
df['End_Time'] = pd.to_datetime(df['End_Time'])

# check datatypes -->
# print(df.dtypes)

# check for null values
# print(df.isnull.any())

df['Date'] = df['End_Time'].dt.date
df['Hour'] = df['End_Time'].dt.hour
df['Weekday'] = df['End_Time'].dt.day_name()
df['Month'] = df['End_Time'].dt.month_name()
df['Year'] = df['End_Time'].dt.year

print(df)





