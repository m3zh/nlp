from pathlib import Path
from tika import parser
import senseToVec as s2v
import spacy
from sense2vec import Sense2VecComponent

## script to create corpus from pdfs
# corpus = ""
# for i in range(3):
#     corpus += s2v.pdf_to_txt(i)
# corpus = nlp.remove_punctuation(corpus)
# with open('../pdfs/corpus.txt','w') as f:
#     f.write(corpus)

# with open('../dictvec/corpus.txt','r') as f:
#     corpus = f.read()
# corpus = list(corpus.replace(r'\n',' ').replace(r'[\d+\\]','').split())

def s2v_synonyms(keyword):
    nlp = spacy.load("en_core_web_sm")
    s2v = nlp.add_pipe("sense2vec")
    s2v.from_disk("../dictvec/vectors_md")
    doc = nlp(keyword)
    assert doc[:].text == keyword
    freq = doc[:]._.s2v_freq
    vector = doc[:]._.s2v_vec
    most_similar = list(doc[:]._.s2v_most_similar(350))
    syns = [s[0][0].lower() for s in most_similar if s[1] > 0.66]
    return (syns)

