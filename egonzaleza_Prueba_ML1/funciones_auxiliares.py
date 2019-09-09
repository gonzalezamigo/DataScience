#!/usr/bin/env python
# coding: utf-8

# # Funciones auxiliares 

import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# añadimos seaborn
import seaborn as sns
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (10, 6)
from sklearn.feature_extraction.text import CountVectorizer

# importamos nltk, descargamos las stop words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('wordnet')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re                      # Regular expressions


import string
from string import punctuation


from nltk.stem.porter import *




def act_more_tweet(df):
    """
    funcion que nos entrega un df con los 
    10 autores que mas tweet hasn escrito
    
    parametros:
    df: el data frame que estamos trabajando

    """
    a= df.groupby('author').content.nunique().reset_index()
    b=a.loc[a['content'] > 3]
    b= b.sort_values(by='content',ascending=False).head(10)
    return b

def remove_pattern(input_txt, pattern):
    """
    funcion que nos remueve las palabras que esten
    acompañadas de estos elemntos string '@[\w]*'
    
    parametros:
    input_txt: en este caso la variable content
    pattern: terminos que eliminaremos

    """
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt 

def just_words(df, variable):
    """
    funcion que nos remueve los demas elementos que no son palabras,
    los non_words
    
    parametros:
    df: df a utilizar
    variable: variable a la que le queremos eliminar los non_words
    """
    # creamos el elemento non_words que contendra punctuation sumado a '¿', '¡' y los numeros del 0 al 9
    non_words = '¿¡0123456789'
    non_words += punctuation
    
    df[variable]= df[variable].str.replace('[{}]'.format(non_words), ' ').str.lower()
       
    return df.head()

def eliminate_litle_words(df, variable):
    """
    funcion que nos remueve las palabras que tienen 
    3 o menos caracteres
    
    parametros:
    df: df a utilizar
    variable: variable a la que le queremos eliminar palabras cortas
    """
    df[variable] = df[variable].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
    return df.head()

def eliminate_stop_words(df, variable):
    """
    funcion que nos remueve las palabras stop_words
    
    parametros:
    df: df a utilizar
    variable: variable a la que le queremos eliminar stop_words
    """
    stop = stopwords.words('english')
    df[variable] = df[variable].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    return df.head()
    
def tokenize(df,variable):
    """
    funcion tokeniza en una nueva variable la variable
    que le pasamos como parametro
    
    parametros:
    df: df a utilizar
    variable: variable a la que le crearemos copia tokenizada
    """
    df['content_recod2'] = df[variable].apply(lambda x: x.split())
    return df.head()


    
def stemming (df,variable):
    """
    funcion que hace el 
    proceso de stemming
    
    parametros:
    df: df a utilizar
    variable: variable a la que le haremos el proceso
    """
    stemmer = PorterStemmer()
    df[variable] = df[variable].apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
    return df.head()
    



def generate_sent():
    """
    funcion retorna aleatoriamente
    la palabra positive y negative
    
    """
    np.random.seed(8934747)
    sent = np.random.choice(['negative', 'positive'])
    return sent