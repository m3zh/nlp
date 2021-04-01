# INSTALLATIONS

The first time you run the script, make sure to install the following in your terminal:

`python3 -m nltk.downloader stopwords`  
`python3 -m nltk.downloader punkt`  
`python3 -m nltk.downloader wordnet`

`pip install -U spacy`
`python -m spacy download en_core_web_sm`

## How To

Run `python3 main.py`  
see your results sorted by relevance in results.csv

## WARNINGS

If you use stemTokenizer and get the following error:

`/home/user/.local/lib/python3.8/site-packages/sklearn/feature_extraction/text.py:388: UserWarning: Your stop_words may be inconsistent with your preprocessing. [...] `

It means some stems are not recognized as stopwords and look inconsistent to the tokenizer.  
Ignore the warning.

## Notes

lemmaTokenizer is slower then stemTokeniner and only slightly more accurate.
