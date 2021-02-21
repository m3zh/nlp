import pandas as pd

# create df
def df_empty_creator():
    df= {'title':[], 'publication date':[],'subject':[], 'DOI':[], 'author':[], 'abstract':[]}
    df= pd.DataFrame(data=df)
    df= df.astype(str)
    df['publication date']= pd.to_datetime(df['publication date'])
    return(df)

df_empty= df_empty_creator()
