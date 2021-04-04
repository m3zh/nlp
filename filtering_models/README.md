# INSTALLATIONS

For NLTK:  

`python3 -m nltk.downloader stopwords`  
`python3 -m nltk.downloader punkt`  
`python3 -m nltk.downloader wordnet`

For SPACY:  

`pip install -U spacy`
`python -m spacy download en_core_web_sm`

For s2v VECTORS:

`cd filter_models/`
`tar -xvf vectors_md.tar.gz`

### WARNING

In case you get the following error:

`raise ValueError(f"Can't read file: {location}")`
`ValueError: Can't read file: ../filtering_models/vectors_md/cfg`

remove the s2v_old folder and re-untar vectors_md.tar.gz
if you still get this error, check your path to the folder s2v_old