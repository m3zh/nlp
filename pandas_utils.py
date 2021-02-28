import pandas as pd

# Create empty DataFrame
def df_empty_creator():
    df= {'title':[], 'publication date':[],'subject':[], 'journal':[], 'DOI':[], 'author':[], 'abstract':[], 'from_database':[]}
    df= pd.DataFrame(data=df)
    df= df.astype(str)
    # Add following line directly to db_df_feeder (may be adapted)
    # df['publication date']= pd.to_datetime(df['publication date'])
    return(df)

def df_full_merging (*argv):
    df= df_empty_creator()
    for arg in argv:
        df= df.append(arg, ignore_index=True)
    return(df)
