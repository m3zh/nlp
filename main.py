from datetime import datetime
import pandas_utils
import search_db.pubmed as search_db_pubmed
import search_db.crossref as search_db_crossref
import search_db.pyscopus as search_db_scopus
import search_db.google_scholar.search_utilities as search_db_gs

# words to research without operators
search_no_operators= "gifted+children+behavior+problems"
# words to research with operators
search_with_operators= "gifted children behavior problems" #OPERATORS doesnt work with pubmed

# DataFrame FEEDERS
## Feed it with PUBMED
df_pubmed= search_db_pubmed.pubmed_df_feeder(search_with_operators)
print("✓ Pubmed, n=", len(df_pubmed))
## Feed it with CROSSREF
df_crossref= search_db_crossref.crossref_df_feeder(search_no_operators)
print("✓ Crossref, n=", len(df_crossref))
## Feed it with ELSEVIER
df_elsevier= search_db_scopus.scopus_df_feeder(search_no_operators)
print("✓ Scopus, n=", len(df_elsevier))

df_gs= search_db_gs.gs_df_feeder(search_no_operators)
print("✓ Google Scholar, n=", len(df_gs))

# Merge DataFrame filled by databases
df_full= pandas_utils.df_full_merging(df_crossref, df_pubmed, df_elsevier, df_gs)
## Print lenght of index (number of rows)
print("Number of results before cleaning :", len(df_full))

# Cleaning the whole set
# df_clean= df_full.drop_duplicates(subset=['DOI'], keep='last')
# df_clean.reset_index(drop=True, inplace=True)
## Print lenght of index (number of rows)
# print("Number of results after cleaning :", len(df_clean))

# Export merged DataFrame to files
df_full.to_csv("./excels/df{}{}.csv".format(search_no_operators, datetime.now().time()))
print("Results exported to .csv in ./excels/")
