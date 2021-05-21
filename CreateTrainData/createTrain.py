import numpy as np 
import pandas as pd 
import nltk
from nltk.corpus import stopwords
import string
import os
path = os.path.dirname(__file__)

lower_map = {
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
    ord(u'Ö'): u'ö',
    ord(u'Ü'): u'ü',
}

data = pd.read_csv("{0}/data.csv".format(path),sep=",",encoding ='utf-8')
WPT = nltk.WordPunctTokenizer()
stop_word_list = nltk.corpus.stopwords.words('turkish')

x = data['Yorum'].copy()
y = pd.DataFrame(data['Duygu'].values.reshape(-1,1), columns = ['Label'])

def text_preprocess(text):
    text = text.translate(lower_map).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stop_word_list]
    return " ".join(text)

x = x.apply(text_preprocess)

trainData = pd.concat([x, y], axis=1)
trainData.to_csv("{0}/trainData.csv".format(path),index=False)