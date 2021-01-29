#how to search terms with GS
#implement proxygenerator module to dont get banned
from scholarly import scholarly

terms_searched = "depression"
result = scholarly.search_pubs(terms_searched)

scholarly.pprint(next(result))


#Crossref
from habanero import Crossref
cr = Crossref()
x = cr.works(query_container_title = "ecology", limit = 10, select="title")
print(x)

x.keys()
x['message'].keys()

#print title of articles
for item in x['message']['items']:
	print(item)
