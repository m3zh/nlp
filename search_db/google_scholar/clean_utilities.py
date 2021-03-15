import re
from bs4 import BeautifulSoup as bs

# clean results of google scholar
## provide only text without weirds characters from html syntax

def text(my_list):
	clean_lst = []
	clean_rgx = re.compile(r'\[.+\]')
	for elem in my_list:
		obj = elem.get_text()
		obj = re.sub(clean_rgx, '', obj)
		clean_lst.append(obj.strip())
	return (clean_lst)

def author(authors_list):
	authors_lst = []
	clean_rgx = re.compile(r'\s-.+')
	for elem in authors_list:
		obj = elem.get_text()
		obj = re.sub(clean_rgx, '', obj)
		authors_lst.append(obj.strip())
	return (authors_lst)

def journal_and_publication_year(authors_list):
	year_lst = []
	journal_lst = []
	year_rgx = re.compile(r'\d{4}')
	journal_rgx = re.compile(r'-\s(.*),\s')
	for elem in authors_list:
		year = re.findall(year_rgx, elem.get_text())
		journal = re.findall(journal_rgx, elem.get_text())
		year_lst.append(''.join(year))
		journal_lst.append(''.join(journal))
	return (journal_lst, year_lst)

# this function is specific for gs
def DOI_list(titles_list):
	DOI_lst = []
	doi_rgx = re.compile(r'.*?(10\..*\d+)(.*)?')
	for elem in titles_list:
		try:
			obj = elem.find('a')['href']
			obj = re.sub(doi_rgx, r"\1", obj) # --> add https.//doi.org to turn doi into link
		except TypeError:
			obj = ""
			pass
		DOI_lst.append(obj.strip())
	return (DOI_lst)

def data(html):
	titles = html.find_all('h3', class_="gs_rt")
	authors = html.find_all(class_='gs_a')
	abstracts = html.find_all(class_='gs_rs')
	journals, years = journal_and_publication_year(authors)
	doi = DOI_list(titles)
	titles = text(titles)
	authors = author(authors)
	abstracts = text(abstracts)
	data = list(zip(titles, years, journals, doi, authors, abstracts))
	return (data)
