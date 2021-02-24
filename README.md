# INSTALLATIONS

The first time you run the script, make sure to install the following in your terminal:
python3 -m nltk.downloader stopwords
python3 -m nltk.downloader punkt
python3 -m nltk.downloader wordnet

## WARNINGS

If you use stemTokenizer and get the following error: \

/home/milena/.local/lib/python3.8/site-packages/sklearn/feature_extraction/text.py:388: UserWarning: Your stop_words may be inconsistent with your preprocessing. Tokenizing the stop words generated tokens ['abov', 'afterward', 'alon', 'alreadi', 'alway', 'ani', 'anoth', 'anyon', 'anyth', 'anywher', 'becam', 'becaus', 'becom', 'befor', 'besid', 'cri', 'describ', [...], 'wherea', 'whereaft', 'wherebi', 'wherev', 'whi', 'yourselv'] not in stop_words.
warnings.warn('Your stop_words may be inconsistent with '

it means some stems are not recognized as stopwords and seems inconsistent to the tokenizer.
Ignore the warning.

## Notes

lemmaTokenizer is slower then stemTokeniner and only slightly more accurate.
