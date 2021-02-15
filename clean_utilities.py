import re
from bs4 import BeautifulSoup as bs

def my_text(my_list):
	clean_lst = []
	clean_rgx = re.compile(r'\[|\]|\bPDF\b|\bHTML\b')
	for elem in my_list:
		obj = elem.get_text()
		obj = re.sub(clean_rgx, '', obj)
		clean_lst.append(obj.strip())
	return (clean_lst)
