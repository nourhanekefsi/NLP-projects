import nltk
import math
import pandas
import numpy
import tokenize
import re

def Preprocess(text, model_name='bert-base-uncased', max_length=512):
    """
    Preprocesses the input text.
    """
    tokenizer = nltk.RegexpTokenizer(r'\[a-zA-Z_]')
    text = tokenizer.tokenize(text)
    text = text.lower()
    stop_words = nltk.corpus.stopwords.words('english')
    text = [token for token in text if token not in stop_words]
    lemmatizer = nltk.WordNetLemmatizer()
    text = [lemmatizer.lemmatize(token) for token in text]
    
    return text

def Vocabulary(text, vocabulary):
    for token in text:
        if token not in vocabulary:
            vocabulary.append(token)
    return vocabulary
            
def Representation(vocabulary, text_list):
    IDF = [0]*len(vocabulary)
    dictionary = [[0]*len(vocabulary)]*len(text_list)
    for i in len(text_list):
        freq = nltk.FreqDist(text_list[i])
        dictionary[i] = [math.log10(freq[j]+1) for j in vocabulary]
        IDF += [math.log10(freq[j]+1) for j in vocabulary]

