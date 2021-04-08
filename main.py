from datetime import datetime
from datetime import date
import os
import filtering_models.main as  main_filtering
import pandas as pd

keywords = ["emotional attachment","gifted"]
# Merge DataFrame filled by databases
df_full = pd.read_csv('csv/gifted-attachment.csv')
## Print lenght of index (number of rows)
print("Number of results before cleaning :", len(df_full))

df_filtered = main_filtering.filtering(df_full, keywords)

df_clean = df_filtered.drop_duplicates(subset=["title"], keep='first')
df_clean.to_csv('df_clean.csv')
print("Df clean :", len(df_clean))