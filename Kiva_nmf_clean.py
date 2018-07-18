import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

import numpy as np
from bs4 import BeautifulSoup
import string


#Step 1. Load the data
df = pd.read_csv('description.csv')
descriptions = df['Description_br_']

#Step 2. Vectorize, Stem and Lemmatize words

# vect = CountVectorizer(stop_words='english')
# model = vect.fit_transform(docs)

snowball = SnowballStemmer('english')
wordnet = WordNetLemmatizer()

def tokenize(doc):
    soup = BeautifulSoup(doc,'html.parser')
    text = soup.get_text()
    translater = str.maketrans('','',string.punctuation)
    a = [wordnet.lemmatize(word) for word in word_tokenize(text.lower().translate(translater))]
    return a

vect = TfidfVectorizer(stop_words='english', analyzer='word',tokenizer=tokenize)
model = vect.fit_transform(descriptions)
features = vect.get_feature_names()

# Step 3. Build NMF model
topic_num = 8

nmf_model = NMF(n_components=topic_num, random_state=1,alpha=.1, l1_ratio=.5)
W = nmf_model.fit_transform(model)
H = nmf_model.components_


# Step 4. Print top 10 features from each cluster


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()

print_top_words(nmf_model,features,10)


# Step 5. Print the details of each cluster

def check_descriptions(i):
    weights = np.sort(W[i])[-5:]
    print('top 5 weights: ', weights)

    sorted_topics = np.argsort(W[i])[-5:]
    print('top 5 sorted topics: ', sorted_topics)

    for topic_idx, topic in enumerate(H):
        if topic_idx == int(sorted_topics[-1]):
            print("Topic #%d:" % topic_idx)
            print(" ".join([features[j]
                        for j in topic.argsort()[:-10 - 1:-1]]))
    print()

    print('Original text: \n', descriptions.iloc[i])


# Step 6. Check the heaviest weights for each cluster
for i in range(topic_num):
    print(f'top 3 weights for topic {i}: ', np.sort(W.T[i])[-3:])
    print(f'top 3 description indexes for topic {i}: ', np.argsort(W.T[i])[-3:])



