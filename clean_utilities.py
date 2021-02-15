import re
from bs4 import BeautifulSoup as bs

def my_text(my_list):
	clean_lst = []
	clean_rgx = re.compile(r'\[')
	for elem in my_list:
		obj = elem.get_text()
		re.sub(clean_rgx, '', obj)
		clean_lst.append(obj)
	return (clean_lst)
