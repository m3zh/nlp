import pandas as pd
from scholarly import scholarly, ProxyGenerator
# how to search terms with GS
# implement proxygenerator module to avoid ban

pg = ProxyGenerator()
pg.Tor_External(tor_sock_port=9050, tor_control_port=9051, tor_password="scholarly_password")
scholarly.use_proxy(pg)


#pubs = next(scholarly.search_pubs('Depression in children'))
queries = next(scholarly.search_keywords(['cannabis','depression']))
author = next(scholarly.search_author('Judy Garber'))
# for query in queries.values():
# 	scholarly.pprint(query)
# query = next(scholarly.search_keywords(['depression','cannabis']))
scholarly.pprint(author)
print(len(queries))
