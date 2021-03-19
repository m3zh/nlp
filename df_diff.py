import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

# to diff two df
def diff_df(df1, df2):
    df3 = pd.concat([df1,df2]).drop_duplicates(keep=False) # works only if df1 and df2 has no duplicates
    print(df1.shape)
    print(df2.shape)
    print(df3.shape)
    df1.to_csv('diff_df1.csv')
    df2.to_csv('diff_df2.csv')
    df3.to_csv('diff_df.csv')
    return df3

# to diff two excels files
def diff_xlsx(df1, df2):
    df1 = pd.read_excel('../Downloads/df1.xlsx', index_col=None, header=None)
    df1.drop_duplicates(inplace=True)
    df2 = pd.read_excel('../Downloads/df2.xlsx', index_col=None, header=None)
    df2.drop_duplicates(inplace=True)
    df3 = pd.concat([df1,df2]).drop_duplicates(keep=False) # works only if df1 and df2 has no duplicates
    print(df1.shape)
    print(df2.shape)
    print(df3.shape)
    df3.to_csv('diff_xlsx.csv')

# to diff two csv files
def diff_csv(df1, df2):
    df1 = pd.read_csv('diff_df1.csv', sep=',')
    df1.drop_duplicates(inplace=True)
    df2 = pd.read_csv('diff_df2.csv', sep=',')
    df2.drop_duplicates(inplace=True)
    df3 = df1[~df1.title.isin(df2.title.values)]
    print(df1.shape)
    print(df2.shape)
    print(df3.shape)
    df3.to_csv('diff_csv.csv')
    return df3

