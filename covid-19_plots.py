#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
from datetime import datetime, timedelta
from os import path
import glob


# In[62]:


date = datetime.today() - timedelta(days = 1)
min_date = datetime(year = 2020, month = 1, day = 22)

data_dir = "data"

while date >= min_date:
    date_formatted = date.strftime("%m-%d-%Y")
    filepath = f"{data_dir}/{date_formatted}.csv"
    if not path.isfile(filepath):    
        url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date_formatted}.csv"
        dataframe = pd.read_csv(url)
        dataframe.to_csv(filepath, index = False)
        print(f"Saved {filepath}")
    else:
        print(f"Skipped {filepath}")
    date = date - timedelta(days = 1)


# In[70]:


data_files = glob.glob(f"{data_dir}/*.csv")

daily_dataframes = []

print(data_files)

for file in data_files:
    daily_dataframe = pd.read_csv(file)
    daily_dataframes.append(daily_dataframe)

combined_data = pd.concat(daily_dataframes, axis=0, ignore_index=True)

print(combined_data)

