import numpy as np 
import pandas as pd 
import nltk
from nltk.corpus import stopwords
import string
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


class SentimentAnalysis:
    lower_map = {
        ord(u'I'): u'ı',
        ord(u'İ'): u'i',
        ord(u'Ö'): u'ö',
        ord(u'Ü'): u'ü',
    }
    data = pd.read_csv("CreateTrainData/trainData.csv",sep=",",encoding ='utf-8')
    x = data['Yorum'].copy()
    y = data['Label'].values.reshape(-1,1)
    WPT = nltk.WordPunctTokenizer()
    stop_word_list = nltk.corpus.stopwords.words('turkish')
    vect = ""
    x_train_vectorized =""
    lr = LogisticRegression()
    def __init__(self):
        self.vect = CountVectorizer(encoding ='utf-8').fit(self.x) # fit and transform
        self.x_train_vectorized = self.vect.transform(self.x)
        self.lr.fit(self.x_train_vectorized, self.y)

    def text_preprocess(self,text):
        text = text.translate(self.lower_map).lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = [word for word in text.split() if word.lower() not in self.stop_word_list]
        return " ".join(text)

    def analysis(self,texts):
        for text in texts:
            text = self.text_preprocess(text)
        predictions = self.lr.predict(self.vect.transform(texts))
        size = predictions.shape[0]
        size2 = predictions[predictions == 1].shape[0]
        return ((size2 * 100) / size)