from datetime import datetime
import pandas_utils
import search_db.pubmed as search_db_pubmed
import search_db.crossref as search_db_crossref
import search_db.elsapy.elsevier as search_db_elsevier
import search_db.pyscopus as search_db_scopus

# words to research without operators
search_no_operators= "gifted+children+behavior+problems"
# words to research with operators
search_with_operators= "gifted children behavior problems" #OPERATORS doesnt work with pubmed

# DataFrame FEEDERS
## Feed it with PUBMED
df_pubmed= search_db_pubmed.pubmed_df_feeder(search_with_operators)
## Feed it with CROSSREF
df_crossref= search_db_crossref.crossref_df_feeder(search_no_operators)

##### TESTING
# (re)initialising of empty DataFrame
## Feed it with ELSEVIER
# df_elsevier= search_db_elsevier.elsevier_df_feeder(df_empty, search_no_operators)
# df_empty= pandas_utils.df_empty_creator()
# df_elsevier = search_db_scopus.scopus_df_feeder(df_empty, search_no_operators)
# display(df_elsevier)

# Merge DataFrame filled by databases
df_full= pandas_utils.df_full_merging(df_crossref, df_pubmed)
## Print lenght of index (number of rows)
print("Number of results before cleaning :", len(df_full))

# Cleaning the whole set
df_clean= df_full.drop_duplicates(subset=['DOI'], keep='last')
## Print lenght of index (number of rows)
print("Number of results after cleaning :", len(df_clean))

# Export merged DataFrame to files
df_clean.to_csv("./excels/df{}{}.csv".format(search_no_operators, datetime.now().time()))
