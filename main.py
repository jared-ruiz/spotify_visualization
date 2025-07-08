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
            print(df)
            
    except:
        print('file name not detected.')
        
