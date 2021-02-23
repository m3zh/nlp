from elsapy.elsclient import ElsClient
import pandas as pd

def elsevier_df_feeder(df, keywords):

    myCl = ElsClient('')
    doc_srch = ElsSearch("star trek vs star wars",'sciencedirect')
    doc_srch.execute(client, get_all = False)
    print ("doc_srch has", len(doc_srch.results), "results.")

    # fill database column
    df['from_database']= 'elsevier'
    # apply date time format to publication date column
    df['publication date']= pd.to_datetime(df['publication date'])
    return(df)
