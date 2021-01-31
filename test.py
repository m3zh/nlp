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
x= cr.works(query= "cannabis+depression", limit= 5, select= ["title","DOI","author", "abstract", "published-print"])

## get full text links, idk the fuck
## x = cr.works(filter = {'has_full_text': True})

## trying to understand data structure
x.keys()
x['message'].keys()
x.type()
## print fields selected of articles
for item in x['message']['items']:
	print(item)
## print only the title of first article, work for any fields if exist
for item in x['message']['items'][0]['title']:
	print(item)
## trying to convert x into dataframe
print(pd.DataFrame(x['message']['items']))
