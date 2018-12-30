# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import math
example_file = open('modi_speech.txt','r')
example_sent = example_file.read().replace('\n','')
print(len(example_sent))
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words ]
filtered_sentence = []
for w in word_tokens:
     if w not in stop_words:
         filtered_sentence.append(w)
print('Token of the speech')
#print(word_tokens)
print()
print('filtered sentence')
#print(filtered_sentence)
print()
num = dict(Counter(filtered_sentence))
#print('word count')
#print(num)
print()
""" speech analysis"""
"""total words spoken by modi"""
print('total words spoken in the speech by modi',len(word_tokens))
print('total words spoken without stop words in the speech by modi',len(filtered_sentence))
print('total unique word spoken',len(num))
print('total stop word spoken',len(word_tokens) - len(filtered_sentence))
total_stop_word = len(word_tokens) - len(filtered_sentence)
percentage_of_stop_word_spoken = (total_stop_word/(len(word_tokens))*100)
print('total percentage of stop word spoken',math.floor(percentage_of_stop_word_spoken),"%")
"""most repeated word in the speech is I """
precentage_of_most_repeated_word = (54/len(filtered_sentence)*100)
print('precentage of most repeated word is',precentage_of_most_repeated_word)


#import nltk
#nltk.download('punkt')

