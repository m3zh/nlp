import pandas as pd

# create empty DataFrame
def df_empty_creator():
    df= {'title':[], 'publication date':[],'subject':[], 'journal':[], 'DOI':[], 'author':[], 'abstract':[]}
    df= pd.DataFrame(data=df)
    df= df.astype(str)
    # add following line directly to db_df_feeder
    # df['publication date']= pd.to_datetime(df['publication date'])
    return(df)
