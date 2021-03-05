import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook


df1 = pd.read_excel('../Downloads/df1.xlsx', index_col=None, header=None)
df2 = pd.read_excel('../Downloads/df2.xlsx', index_col=None, header=None)

df3 = pd.concat([df1,df2]).drop_duplicates(keep=False) # works only if df1 and df2 has no duplicates
df3.to_excel('diff(res1-res2).xlsx')

# check if difference in number of rows is consistent
print(df1.shape)
print(df2.shape)
print(df3.shape)
