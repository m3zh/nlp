import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

# to diff two excels files
# df1 = pd.read_excel('../Downloads/df1.xlsx', index_col=None, header=None)
# df2 = pd.read_excel('../Downloads/df2.xlsx', index_col=None, header=None)
# df3 = pd.concat([df1,df2]).drop_duplicates(keep=False) # works only if df1 and df2 has no duplicates

# to diff two csv files
df1 = pd.read_csv('../Downloads/new.csv', sep=',')
df1.drop_duplicates(inplace=True)
df2 = pd.read_csv('../Downloads/results.csv', sep=',')
df2.drop_duplicates(inplace=True)
df3 = df1[~df1.title.isin(df2.title.values)]

# common part
df3.to_excel('diff(complete-results).xlsx')

# check if difference in number of rows is consistent
print(df1.shape)
print(df2.shape)
print(df3.shape)
