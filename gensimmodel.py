import gensim
import spacy
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
# from gensim.models.wrappers import LdaMallet
from gensim.models.phrases import Phrases, Phraser
from gensim.corpora.dictionary import Dictionary
from gensim.models import Phrases
import warnings
warnings.filterwarnings('ignore',category=DeprecationWarning)

def filter_topics(model, corpus, df):
    # keyword = 'gifted'
    # filtered = []
    # topic_words = model.show_topics(num_topics=20, num_words=50,formatted=True)
    # for t,s in topic_words:
    #     if keyword in s:
    #         filtered.append(t)
    # print(filtered)
    # mask = df['topics'].isin(filtered)
    # df = df[mask]
    topics = []
    model = gensim.models.wrappers.ldamallet.malletmodel2ldamodel(model)
    t = model.get_term_topics("attachment", minimum_probability=0.05)
    for i,j in t:
        topics.append(i)
    df = df[df['topics'].isin(topics)]
    return df

def get_topics(model, corpus):
    topics = []
    for i, row in enumerate(model[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic, prop) in enumerate(row):
            if j == 0:  # => dominant topic
                t = model.show_topic(topic)
                topics.append(int(topic))
            else:
                break
    return(topics)

def mallet_model(tagged):
    mallet_path = '../Downloads/mallet-2.0.8/bin/mallet' # update this path
    id2word = corpora.Dictionary(tagged)
    id2word.save_as_text('id2word.dict')
    corpus = [id2word.doc2bow(t) for t in tagged]
    mallet_model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, id2word=id2word, num_topics=20)
    return corpus, mallet_model

def lda_model(tagged):
    id2word = corpora.Dictionary(tagged)
    #id2word.save('id2word.dict')
    corpus = [id2word.doc2bow(t) for t in tagged]
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=20,
                random_state=100, update_every=1, chunksize=100, passes=10, alpha='auto', per_word_topics=True)
    return corpus, lda_model

def lemmas_and_pos(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    lang = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    tagged = []
    for sent in texts:
        doc = lang(" ".join(sent))
        tagged.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return tagged

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True)) # deacc=True removes punctuations

def get_grams(texts):
    words = list(sent_to_words(texts))
    bigram = Phraser(Phrases(words, min_count=5, threshold=100)) # higher threshold fewer phrases.
    trigram = Phraser(Phrases(bigram[words], threshold=100))
    bi = [bigram[w] for w in words]
    tri = [trigram[bigram[w]] for w in words]
    return bi, tri

def get_model(df, texts):
    bigrams, trigrams = get_grams(texts)
    tagged_corpus = lemmas_and_pos(bigrams)
    corpus, model = mallet_model(tagged_corpus)
    #print(model.show_topics())
    df['topics'] = get_topics(model, corpus)
    df = filter_topics(model, corpus, df)
    #mask = df['topics'].isin(filtered)
    df = df.drop('topics', axis=1)
    df.to_csv('topicsgensim.csv')
    print(df.shape)
    return (df)