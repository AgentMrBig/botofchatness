# This is a smart chatbot ment to build quality articles of 1000 to 1500 words long

# Import libraries
from newspaper import Article
import random
import string
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np 
import warnings

warnings.filterwarnings('ignore')

#Get the article
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')

article.download() 
article.parse()
article.nlp() 
corpus = article.text  

print(corpus)