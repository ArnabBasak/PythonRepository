import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict

stop_words = set(stopwords.words('english'))
#print(type(stop_words))
input_sentence = "this is a .......!@#sentense sentense written written by me at a spider editor"
word_tokens = word_tokenize(input_sentence)
print(word_tokens)

#filtered_sentences = [w for w in word_tokens if not w in stop_words]
#filtered_sentences = []
#for w in word_tokens:
#    if w not in stop_words:
#        filtered_sentences.append(w)
##print(word_tokens)
##print(filtered_sentences) 
##print(filtered_sentences)
#appearences = defaultdict(int)
#for x in filtered_sentences:
#    appearences[x]+= 1
#    print(x,appearences[x])
    