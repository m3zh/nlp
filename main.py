from datetime import datetime
from datetime import date
import os
import zipfile
import pandas_utils
import search_db.pubmed as search_db_pubmed
import search_db.crossref as search_db_crossref
# import search_db.pyscopus as search_db_scopus
import search_db.google_scholar.search_utilities as search_db_gs
import search_db.frontiersin as search_db_frontiersin
import filtering_models.main as  main_filtering
import pandas as pd

# words to research without operators
search_no_operators = "gifted+attachment"
# words to research with operators
search_with_operators = "gifted attachment" #OPERATORS doesnt work with pubmed
# name of client
name_client = input('Please enter name of client : ')
id_results = str("{0}_{1}_{2}".format(name_client, search_no_operators, date.today()))
# create client's folder
os.mkdir("./results/{0}".format(id_results))
# create file to store effectvive count (PRISMA method)
prisma_file = open("./results/{0}/records_numbers.txt".format(id_results),"w+")



# DataFrame FEEDERS
## Feed it with PUBMED
# df_pubmed = search_db_pubmed.pubmed_df_feeder(search_with_operators)
# print("✓ Pubmed, n =", len(df_pubmed))
# prisma_file.write("Pubmed, n=" + str(len(df_pubmed)) + "\n")
# # Feed it with CROSSREF
# df_crossref = search_db_crossref.crossref_df_feeder(search_no_operators)
# print("✓ Crossref, n =", len(df_crossref))
# prisma_file.write("Crossref, n=" + str(len(df_crossref)) + "\n")
# # Feed it with ELSEVIER
# df_elsevier = search_db_scopus.scopus_df_feeder(search_no_operators)
# print("✓ Scopus, n =", len(df_elsevier))
# prisma_file.write("Scopus, n=" + str(len(df_elsevier)) + "\n")
# # Feed it with GOOGLE SCHOLAR
df_gs = search_db_gs.gs_df_feeder(search_no_operators)
print("✓ Google Scholar, n =", len(df_gs))
prisma_file.write("Google Scholar, n=" + str(len(df_gs)) + "\n")
## Feed it with FRONTIERSIN
df_frontiersin = search_db_frontiersin.frontiersin_df_feeder(search_no_operators)
print("✓ Frontiersin, n =", len(df_frontiersin))
prisma_file.write("Frontiersin, n=" + str(len(df_frontiersin)) + "\n")

# Merge DataFrame filled by databases
df_full = pandas_utils.df_full_merging(df_gs, df_frontiersin) # df_pubmed, df_crossref, df_elsevier
## Print lenght of index (number of rows)
print("Number of results before cleaning :", len(df_full))
prisma_file.write("\n" + "Records identified trough databases searching, n=" + str(len(df_full)) + "\n")
# Export merged DataFrame to files
df_full.to_csv("results/{0}/df_full.csv".format(id_results))

# df_full = pd.read_csv("./results/dfgifted+attachment19:50:05.795009.csv")


# Sorting model
## took a df.csv and return df.xlsx
df_filtered = main_filtering.filtering(df_full)
print("Records dropped while sorting :", (len(df_full)-len(df_filtered)))
prisma_file.write("Records dropped while filtering, n=" + str(len(df_full)-len(df_filtered)) + "\n")

# df_clean = df_filtered

# df_clean = df_filtered.sort_values(by="tdidf_score")

# Cleaning the whole set
# df_clean= df_full.drop_duplicates(subset=['DOI'], keep='last')
# df_clean.reset_index(drop=True, inplace=True)
# df_clean= (df_full.sort_values(by="abstract", na_position='last')
#             .drop_duplicates(subset='DOI', keep='first'))
df_clean = df_filtered.drop_duplicates(subset=["title"], keep='first')
print("Records dropped while duplicates removal :", (len(df_full)-len(df_clean)))
prisma_file.write("Records dropped while duplicates removal, n=" + str(len(df_full)-len(df_clean)) + "\n")
df_clean.to_csv("./results/{0}/df_clean.csv".format(id_results))



# Client's df cleaning
# df_client = df_clean
df_client = df_clean.drop(['from_database'], axis=1)
df_client = df_client.drop(["tfidf_score"], axis=1)
# df_client = df_client.reset_index() GOAL : delete first column
print("Results exported ./results/{0}/, n={1}".format(id_results, len(df_client)))
prisma_file.write("Total records identifed, n=" + str(len(df_client)) + "\n")
# Close PRISMA file
prisma_file.close()
df_client.to_csv("./results/{0}/results.csv".format(id_results))


# Print results in console
## Write PRISMA records



# Create and export to zip
final_zip = zipfile.ZipFile("./results/{0}/{0}.zip".format(id_results), "w", zipfile.ZIP_DEFLATED)
final_zip.write("./results/{0}/results.csv".format(id_results))
final_zip.write("./results/{0}/records_numbers.txt".format(id_results))
final_zip.close()
