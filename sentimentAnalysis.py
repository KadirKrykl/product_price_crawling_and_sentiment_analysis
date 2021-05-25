import numpy as np 
import pandas as pd 
import nltk
from nltk.corpus import stopwords
import string
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


class SentimentAnalysis:
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
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = [word for word in text.split() if word.lower() not in stop_word_list]
        return " ".join(text)

    def analysis(self,texts):
        texts = np.array(texts)
        texts = texts.apply(text_preprocess)
        predictions = lr.predict(vect.transform(texts))
        row, col = predictions.shape
        row2, col2 = predictions[predictions == 1].shape
        return ((col2 * 100) / col)