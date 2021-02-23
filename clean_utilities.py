import re
from nltk.corpus import stopwords
import pandas as pd

def stop_words(original):
	sw_list = set(stopwords.words('english')) # you need to download the corpus on your machine -> python3 -m nltk.downloader stopwords
	new = original.applymap(lambda col: [x.lower() for x in str(col).split()])
	new = new.applymap(lambda col: ' '.join([w for w in col if w not in sw_list]))
	return (new)
