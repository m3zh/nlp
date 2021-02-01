import pandas as pd

# how to search terms with GS
# implement proxygenerator module to avoid ban
from scholarly import scholarly

terms_searched = "depression"
result = scholarly.search_pubs(terms_searched)

scholarly.pprint(next(result))


# Crossref
from habanero import Crossref
cr = Crossref()
## return fields selection in a list, fields allowed for selection are :
## abstract, URL, member, posted, score, created,
## degree, update-policy, short-title, license, ISSN, container-title, issued, update-to,
## issue, prefix, approved, indexed, article-number, clinical-trial-number, accepted, author,
## group-title, DOI, is-referenced-by-count, updated-by, event, chair, standards-body, original-title,
## funder, translator, archive, published-print, alternative-id, subject, subtitle, published-online,
## publisher-location, content-domain, reference, title, link, type, ##publisher, volume, references-count,
## ISBN, issn-type, assertion, deposited, page, content-created, short-container-title, relation, editor
limit= 5
x= cr.works(query="cannabis+depression", limit=limit, select=["title","DOI","author", "abstract", "published-print"])

## get full text links, idk the fuck
## x = cr.works(filter = {'has_full_text': True})

## trying to understand data structure
x.keys()
x['message'].keys()
x.type()
## print fields selected of articles
for a in x['message']['items']:
	print(a)
## print only the title of first article, work for any fields if exist
for b in x['message']['items'][0]['title']:
	print(b)

## create df for fields
df= {'title':[], 'DOI':[], 'author':[], 'abstract':[], 'publication date':[]}
df= pd.DataFrame(data=df)
## convert query results to df
def xtodf():
	count= 0
	while (count < limit):
		for item in x['message']['items'][count]['title']:
			count = count + 1
			df.append(item) ## wont work
xtodf()
df
