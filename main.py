from datetime import datetime
import pandas_utils as pandas_utils
import search_db.pubmed as search_db_pubmed
import search_db.crossref as search_db_crossref

# words to research without operators
search_no_operators= "cannabis+depression"
# words to research with operators
search_with_operators= "cannabis AND depression"

# DataFrame FEEDERS
# (re)initialising of empty DataFrame
## Feed it with PUBMED
df_empty= pandas_utils.df_empty_creator()
df_pubmed= search_db_pubmed.pubmed_df_feeder(df_empty, search_with_operators)
# (re)initialising of empty DataFrame
## Feed it with CROSSREF
df_empty= pandas_utils.df_empty_creator()
df_crossref= search_db_crossref.crossref_df_feeder(df_empty, search_no_operators)

# Merge DataFrame filled by databases
df_full= pandas_utils.df_full_merging(df_crossref, df_pubmed)

#Cleaning the whole set
df_full = df_full.drop_duplicates(subset=['DOI'], keep='last')

# Export merged DataFrame to excel file
df_full.to_excel("./excels/df{}{}.xlsx".format(search_no_operators, datetime.now().time()))
