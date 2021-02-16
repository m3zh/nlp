import re
from bs4 import BeautifulSoup as bs

def my_text(my_list):
	clean_lst = []
	clean_rgx = re.compile(r'\[.+\]')
	for elem in my_list:
		obj = elem.get_text()
		obj = re.sub(clean_rgx, '', obj)
		clean_lst.append(obj.strip())
	return (clean_lst)

def my_author(authors_list):
	authors_lst = []
	clean_rgx = re.compile(r'\s-.+')
	for elem in authors_list:
		obj = elem.get_text()
		obj = re.sub(clean_rgx, '', obj)
		authors_lst.append(obj.strip())
	return (authors_lst)

def my_publication_year(authors_list):
	year_lst = []
	extract_rgx = re.compile(r'\d{4}')
	for elem in authors_list:
		year = re.findall(extract_rgx, elem.get_text())
		year_lst.append(''.join(year))
	return (year_lst)

def my_DOI(titles_list):
	DOI_lst = []
	doi_rgx = re.compile(r'.+/doi/abs')
	for elem in titles_list:
		obj = elem.find('a')['href']
		obj = re.sub(doi_rgx, 'https://doi.org', obj)
		DOI_lst.append(obj.strip())
	return (DOI_lst)
