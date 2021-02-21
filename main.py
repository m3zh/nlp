import pandas_utils as pandas_utils
import _search_db.pubmed as search_db_pubmed

#storing of empty DataFrame
df_empty= pandas_utils.df_empty_creator()


df_full_pubmed= search_db_pubmed.pubmed_df_feeder(df_empty, )
