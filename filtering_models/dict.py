import spacy
from sense2vec import Sense2VecComponent
from tika import parser
import re

def pdf_to_txt(pdf):
    with open('../dictvec/'+str(pdf)+'.pdf','rb') as pdf:
        raw = str(parser.from_file(pdf))
        text = raw.encode('utf-8', errors='ignore')
    return(raw.lower())

def custom_corpus():
    corpus = ""
    for i in range(3):
        corpus += pdf_to_txt(i)
    corpus = nlp.remove_punctuation(corpus)
    with open('../pdfs/corpus.txt','w') as f:
        f.write(corpus)
    with open('../pdfs/corpus.txt','r') as f:
        corpus = f.read()
    corpus = list(corpus.replace(r'\n',' ').replace(r'[\d+\\]','').split())
    return (corpus)

def s2v_synonyms(keyword):
    nlp = spacy.load("en_core_web_sm")
    s2v = nlp.add_pipe("sense2vec")
    s2v.from_disk("vectors_md/")
    doc = nlp(keyword)
    assert doc[:].text == keyword
    freq = doc[:]._.s2v_freq
    vector = doc[:]._.s2v_vec
    most_similar = list(doc[:]._.s2v_most_similar(350))
    syns = [s[0][0].lower() for s in most_similar if s[1] > 0.66]
    syns = [re.sub(r'[^a-zA-Z\s:]', '', s) for s in syns]
    return (syns)

def update_dict(keyword, dict):
    if keyword not in dict:
        print("--------------------------------------------")
        print("Getting s2v synonyms ...")
        dict[keyword] = s2v_synonyms(keyword)
    print("Synonyms currently in dictionary:")
    print(','.join(dict[keyword]))
    user_syns = input("Wanna add other synonyms? Write them in a comma-separated list, e.g. my, wonderful synonyms,list\n").split(',').remove('')
    if user_syns:
        user_syns = [s.strip() for s in user_syns]
        dict[keyword].append(w for w in user_syns if w not in dict[keyword])
    to_del = input("Wanna delete any synonyms? Write them in a comma-separated list, e.g. my, wonderful synonyms,list\n").split(',').remove('')
    if to_del:
        to_del = [t.strip() for t in to_del]
        for d in to_del:
            try:
                dict[keyword].remove(d)
            except ValueError:
                pass
    print("----------- dictionary updated -------------")
    return (dict)