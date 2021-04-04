import re
from bs4 import BeautifulSoup as bs

# clean results of google scholar
## this code is tailor-made for gs html, wouldn't work on other html
## provide only text without weirds characters from html syntax

# take a list of dirty titles
## and return a list of clean titles
def text(my_list):
	clean_lst = []
	# removes all [PDF], [HTML], [BOOK] tags
	clean_rgx = re.compile(r'\[.+\]')
	for elem in my_list:
		obj = elem.get_text()
		obj = re.sub(clean_rgx, '', obj)
		# removes trailing spaces
		clean_lst.append(obj.strip())
	return (clean_lst)

# authours list before cleaning looks like: author - year - journal
## take an author list and extracts eveything before the first dash
## returns a list of clean authors
def author(authors_list):
	authors_lst = []
	clean_rgx = re.compile(r'\s-.+')
	for elem in authors_list:
		obj = elem.get_text()
		obj = re.sub(clean_rgx, '', obj)
		authors_lst.append(obj.strip())
	return (authors_lst)

# authours list before cleaning looks like: author - year - journal
## take an author list and extracts the year and eveything after the last dash
## returns two lists, of journals and publication years respectively
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

# titles in gs have a link to the original article
## the functions extracts the link
## if the link contains the article DOI, the DOI is extracted and cleaned
## else the link is preserved
## returns a list of links or DOIs when found
def DOI_list(titles_list):
	DOI_lst = []
	doi_rgx = re.compile(r'.*?(10\..*\d+)(.*)?')
	for elem in titles_list:
		try:
			obj = elem.find('a')['href']
			obj = re.sub(doi_rgx, r"\1", obj) #
		except TypeError:
			obj = ""
			pass
		DOI_lst.append(obj.strip())
	return (DOI_lst)

## takes all html extracted from the current gs page
## cleans it and stocks it in lists by title, doi, etc.
## lists are then zipped in order to create a df in ./gs.py/create_gs_df
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
