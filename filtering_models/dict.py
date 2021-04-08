import spacy
import nltk
from sense2vec import Sense2VecComponent,Sense2Vec
from Levenshtein import distance as lev
from tika import parser
import re
from pathlib import Path
import getch

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

def get_closest_keyword(keyword):
    path = Path(__file__).parent.joinpath('s2v_old')
    s2v = Sense2Vec().from_disk(path)
    words = list(s2v.keys())
    words = [re.sub(r'/r/|/|\|\w+$','',w.replace(r'_',' ').lower()) for w in words]
    distances = ((lev(keyword,word), word) for word in words)
    closest = min(distances)
    return (closest[1])

def s2v_synonyms(keyword, s2v, nlp):
    doc = nlp(keyword)
    assert doc[:].text == keyword
    freq = doc[:]._.s2v_freq
    vector = doc[:]._.s2v_vec
    try:
        most_similar = list(doc[:]._.s2v_most_similar(15))
    except ValueError:
        word = get_closest_keyword(keyword)
        print("No synonyms found in sense2vec.")
        print("Closest word found is: \033[1;31;40m " + word + "\033[0m. Find synonyms for this one? Press y for yes, Enter to skip.")
        choice = getch.getch()
        if choice == 'y':
            return s2v_synonyms(word,s2v,nlp)
        return ([])
    syns = [s[0][0].lower() for s in most_similar if s[1] > 0.66]
    syns = [re.sub(r'[^a-zA-Z\s:]', '', s) for s in syns]
    print(syns)
    return (list(syns))

def load_s2v():
    nlp = spacy.load("en_core_web_sm")
    s2v = nlp.add_pipe("sense2vec")
    path = Path(__file__).parent.joinpath('s2v_old')
    s2v.from_disk(path)
    return (nlp, s2v)

def update_dict(keywords, dict):
    nlp, s2v = load_s2v()
    for k in keywords:
        if k not in dict:
            print("--------------------------------------------")
            print("Getting s2v synonyms for \033[1;33;40m" + k + "\033[0m ...")
            syns = s2v_synonyms(k,s2v,nlp)
            if syns != []:
                print("Synonyms currently in dictionary:")
                print("\033[1;33;40m>>>\033[0m " + ','.join(syns))
            else:
                print("No synonyms for \033[1;33;40m" + k + "\033[0m currently in dictionary.")
            user_syns = input("Wanna add your own synonyms? Write them in a comma-separated list, e.g. my, wonderful synonyms,list\n").split(',')
            try:
                user_syns = [s.strip() for s in user_syns]
                syns = set(syns.extend(user_syns))
            except TypeError:
                pass
            to_del = input("Wanna delete any synonyms? Write them in a comma-separated list, e.g. my, wonderful synonyms,list\n").split(',')
            try:
                to_del = [t.strip() for t in to_del]
                for d in to_del:
                    try:
                        syns.remove(d)
                    except ValueError:
                        pass
            except TypeError:
                pass
            print(syns)
            dict[k] = syns
    print("----------- dictionary updated -------------")
    return (dict)


