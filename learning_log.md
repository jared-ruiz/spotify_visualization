# Learning Log 📚
### General Project Goals

- Explore my Spotify data dating back well within 2024 to current 2025 listening
- Learn best practice when handling data like this, utilizing SQL, Pandas, Tableau and other libraries as needed
- End project with a clean Tableau visualization

Along the way, I will document all the sources and information I pull from to better help my learning experience. I am a visual learner and will link to particular videos and articles throughout the entirety of this document. 

# Day 0 Initial Set Up

I begin my project by cloning my empty repo to my local setup, creating a gitignore file and adding in my newly downloaded json data. This data seems to be formatted pretty standard. I learned recently about [New Line Delimited JSON Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-ndjson) when playing around with some other data and realized there is a bit more set up involved when handling it. 

I also created a [Python Virtual Environment](https://www.w3schools.com/python/python_virtualenv.asp) to house any unique dependencies utilized in this project.

## Quick Cheat Sheet For Handling venv Activation:
### Create venv:
> python -m venv [chosen name of venv directory]
### Activate venv:
> [chosen name of venv directory]\Scripts\activate
### Deactivate venv:
> deactivate
### Delete venv
> rmdir /s /q [chosen name of venv directory]

---

## Initial Data Handling
I have been researching the distinction between using pandas and sqlite for a few days and I think the consensus is I am to use both, pandas would be good for preprocessing the data before pushing it into sqlite for further querying. 

With that being said, I wanted to do a quick crash course on pandas and how it will work for me in this project. 

To test out pandas right out the gate, I wrote up something simple like this:

```
# acquire json title
data_file = input("Please provide your data file for utilization: ")

# handle quick user enter input
if len(data_file) < 3:
    data_file = 'json_data/StreamingHistory_music_0.json'
    df = pd.read_json(data_file)
    print(df)
        
else:
    print('file name not detected.')
```

This outputted a condensed table within my terminal like this:
```
Please provide your data file for utilization: 
               endTime                 artistName                                          trackName  msPlayed
0     2024-06-20 00:58                 The Garden                                 Filthy Rabbit Hole    159740
1     2024-06-23 00:19              Future Magics                                      High With You     22507
2     2024-06-23 00:31                 Effoharkay                                            For Now    175000
3     2024-06-23 00:36                    on4word                                    Alberto Balsalm    303571
4     2024-06-23 00:38                 Windows 96                                        Victim Less    131633
...                ...                        ...                                                ...       ...
6555  2025-06-23 21:29                 essenceォ液ー                      Online Shopping | オンラインショッピング    206778
6556  2025-06-23 21:31                 Vaporwavez                  Advanced Shopping Mall Technology    162000
6557  2025-06-23 21:34                 SPORTSGIRL                                          Hydration    152693
6558  2025-06-23 23:54  L a z u l i _ y e l l o w                                Spanish Pizza Class     54470
6559  2025-06-23 23:57                John Powell  Test Drive - From How To Train Your Dragon Mus...    146840

[6560 rows x 4 columns]
```

From here I referenced the pandas documentation to then get introduced to [DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)

Along with my exploration of pandas, I decided to download [Jupyter Notebook](https://jupyter.org/install) to better visualize what I am doing and to practice a bit off of vscode. I am aware that I can view my pandas output within terminal but since this seems to be an avenue data scientist's use often, I thought it would be a fun way to learn as much as possible. I recreated my original python scripts within my notebook and added in some custom options to change how my pandas was outputting in it's cell. 

I can see the use case for this tool right out of the gate. It's very easy to understand and it visualizes your python and data work locally and with each line of code running in it's own block. You can see step by step what is going on and probably helps diagnose a lot of problems during the data process.

## Day 1 - Start of cleaning

I spent the later part of yesterday watching cleaning tutorials with different types of data files. One I latched onto was for a standard .csv file. The gentleman was taking excel data of rugby players and their stats, and utilizing Jupyter Notebook to adjust column names, add in new ones, and cut out unwanted duplicates and empty spaces. That is what I am going to do today, using his examples as reference - [Real World Data Cleaning in Python Pandas (Step by Step)](https://youtu.be/iaZQF8SLHJs?si=pZOBMWtJTpWn-Grt)

### Game Plan
* Adjust column names to make them easier to read.
* Convert endTime column into a more readable format
* Locate duplicates and null values and evaluate if I want to keep them (for use in analysis for most frequent songs played) or keep everything 1 of.
* Convert milliseconds to seconds for easier reading

To begin, I utilize the rename method within pandas to adjust my DataFrame's current naming scheme as so:

```
# Adjust dataframe columns
df = df.rename(columns={
     'endTime': 'End_Time',
     'artistName': 'Artist',
     'trackName': 'Track',
     'msPlayed': 'Seconds_Played'
     })

print(df)
```

This worked out perfectly! I began looking into how to format the End_Time column since I knew I wanted to separate the date and time into their own columns. First, having the column consist of datetime objects as opposed to being a string would be beneficial for me going forward, especially since I will be exporting this DataFrame into SQL once I am done. I found an article that helped me easily convert and check the data types afterwards: ['Convert column type from string to datetime format in Pandas dataframe'](https://www.geeksforgeeks.org/pandas/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/)

I confirmed the successful type change again using the <ins>df.dtypes</ins> function.

```
End_Time          datetime64[ns]
Artist                    object
Track                     object
Seconds_Played             int64
dtype: object
```


