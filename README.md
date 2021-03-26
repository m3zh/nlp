# INSTALLATIONS and DOWNLOADS

The first time you run the script, make sure to install the following in your terminal:

`python3 -m nltk.downloader stopwords`  
`python3 -m nltk.downloader punkt`  
`python3 -m nltk.downloader wordnet`

To use gensim topic modelling download:  

https://www.machinelearningplus.com/wp-content/uploads/2018/03/mallet-2.0.8.zip (and update the path in your model to the correct download folder)
`python -m spacy download en</pre>`
`sudo pip3 install -U gensim`

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
