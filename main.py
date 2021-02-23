from datetime import datetime
import pandas_utils as pandas_utils
import search_db.pubmed as search_db_pubmed
import search_db.crossref as search_db_crossref
import search_db.elsapy.elsevier as search_db_elsevier

# words to research without operators
search_no_operators= "gifted+children+behavior+problems"
# words to research with operators
search_with_operators= "gifted children behavior problems" #OPERATORS doesnt work with pubmed

# DataFrame FEEDERS
# (re)initialising of empty DataFrame
## Feed it with PUBMED
df_empty= pandas_utils.df_empty_creator()
df_pubmed= search_db_pubmed.pubmed_df_feeder(df_empty, search_with_operators)
df_pubmed.to_csv("./excels/pubmed.csv")
# (re)initialising of empty DataFrame
## Feed it with CROSSREF
df_empty= pandas_utils.df_empty_creator()
df_crossref= search_db_crossref.crossref_df_feeder(df_empty, search_no_operators)
df_crossref.to_csv("./excels/crosref.csv")

##### TESTING
# (re)initialising of empty DataFrame
## Feed it with ELSEVIER
# df_empty= pandas_utils.df_empty_creator()
# df_elsevier= search_db_elsevier.elsevier_df_feeder(df_empty, search_no_operators)
# display(df_elsevier)

# Merge DataFrame filled by databases
# df_full= pandas_utils.df_full_merging(df_crossref, df_pubmed) not working with big n
df_test= df_crossref.append(df_pubmed, ignore_index=True)

# Cleaning the whole set
# df_full= df_full.drop_duplicates(subset=['DOI'], keep='last')


# Export merged DataFrame to files
df_test.to_csv("./excels/df{}{}.csv".format(search_no_operators, datetime.now().time()))
# df_test.to_excel("./excels/dftest3{}{}.xlsx".format(search_no_operators, datetime.now().time()))
