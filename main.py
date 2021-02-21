import pandas_utils as pandas_utils
import search_db.pubmed as search_db_pubmed
import search_db.crossref as search_db_crossref

#storing of empty DataFrame
df_empty= pandas_utils.df_empty_creator()
display(df_empty)

# words to research without operators
search_no_operators= "cannabis+depression"
# words to research with operators
search_with_operators= "cannabis AND depression"

# Empty DataFrame feeders
## pubmed
df_full_pubmed= search_db_pubmed.pubmed_df_feeder(df_empty, search_with_operators)
display(df_full_pubmed)
## crossref
df_full_crossref= search_db_crossref.crossref_df_feeder(df_empty, search_no_operators)
display(df_full_crossref)