import pandas as pd
from scholarly import scholarly, ProxyGenerator
import re
import itertools
from itertools import *
# how to search terms with GS
# implement proxygenerator module to avoid ban

pg = ProxyGenerator()
pg.Tor_External(tor_sock_port=9050, tor_control_port=9051, tor_password="scholarly_password")
scholarly.use_proxy(pg)

keywords = list(filter(None, ["computer","employment","","",""])) #enter your keywords and remove empty words
#regex = '.+?'.join(keywords) #search fr titles containing any of these keywords
#search = re.compile(r'\bcomputer\b.+\bdepression\b', re.I)
#print(re.match(regex, 'computer-base  in everyday life'))

#pubs = iter(scholarly.search_pubs(r'depression'))
queries = scholarly.search_keywords(['cannabis','depression'])
#author = next(scholarly.search_author('Judy Garber'))
# for query in queries.values():
# 	scholarly.pprint(query)
#query = next(scholarly.search_keywords(['depression','cannabis']))
#for query in itertools.islice(queries, 2, None):
	#scholarly.pprint(query)
scholarly.pprint(next(queries))
