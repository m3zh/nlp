import ds_basics as ds
import nlp_basics as nlp
import topicmodel as topic
import similaritymodel as similarity
import gensimmodel as gens
import df_diff as diff
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# reading and cleaning data
df = pd.read_csv('gifted.csv', delimiter=',', usecols=[1,2,3,4,5,6,7,8])
df.drop_duplicates(inplace=True,subset=['title'])
# drop unrelated subjects
# df = ds.check_df(df)
print(df.head(10))
# change title+abstract into a unique column of text
dataset = df.filter(['title','abstract'], axis=1)
dataset['text'] = df['title'].str.cat(df[['abstract']].astype(str), sep=" ")
# remove stopwords and Nan values
# remove academic-reated words
dataset = nlp.normalize(dataset)
dataset = nlp.remove_academic_words(dataset)
# change dataset['text'] into a simple list
texts = dataset['text'].tolist()
# df1 : only similarity
df1 = similarity.get_model(df, texts)
df1.to_csv('df1.csv', sep=',')

# df2: topic + similarity
# df2 = topic.get_model(df, texts)
df2 = gens.get_model(df, texts)
dataset = df2.filter(['title','abstract'], axis=1)
dataset['text'] = df2['title'].str.cat(df2[['abstract']].astype(str), sep=" ")
texts = dataset['text'].tolist()
df2 = similarity.get_model(df2, texts)
print(df2.shape)
#
# df3: diff(df1 - df2)
df3 = diff.diff_df(df1,df2)