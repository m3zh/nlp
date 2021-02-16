import re
import requests
from bs4 import BeautifulSoup as bs

def empty_DOI(lst):
	DOI_lst = []
	for doi in lst:
		if not re.search('\bdoi\b', doi):
			print('NO DOI')
			page = requests.get(doi)
			soup = bs(page.content, "html.parser")
			if re.match(r'.+sciencedirect', doi):
				try:
					doi = soup.select_one('.doi').get_text()
				except None:
					doi = '---'
			elif re.match(r'.+proquest', doi):
				doi = soup.select_one('#text').get_text().replace('DOI:', 'https://doi.org/')
		DOI_lst.append(doi.strip())
	return (DOI_lst)
