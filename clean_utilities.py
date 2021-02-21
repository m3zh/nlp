import re
from bs4 import BeautifulSoup as bs

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

def publication_year(authors_list):
	year_lst = []
	extract_rgx = re.compile(r'\d{4}')
	for elem in authors_list:
		year = re.findall(extract_rgx, elem.get_text())
		year_lst.append(''.join(year))
	return (year_lst)

def DOI(titles_list):
	DOI_lst = []
	doi_rgx = re.compile(r'.+/doi/abs')
	for elem in titles_list:
		try:
			obj = elem.find('a')['href']
			obj = re.sub(doi_rgx, 'https://doi.org', obj)
		except TypeError:
			obj = ""
			#print("empty value")
			pass
		DOI_lst.append(obj.strip())
	return (DOI_lst)

def data(html):
	titles = html.find_all('h3', class_="gs_rt")
	authors = html.find_all(class_='gs_a')
	abstracts = html.find_all(class_='gs_rs')
	years = publication_year(authors)
	doi = DOI(titles)
	titles = text(titles)
	authors = author(authors)
	abstracts = text(abstracts)
	data = list(zip(authors, titles, abstracts, years, doi))
	return (data)
