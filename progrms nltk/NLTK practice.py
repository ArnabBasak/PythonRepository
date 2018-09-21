import os
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
filecheck = os.path.isfile('E:\python programs\progrms nltk\corpus.txt')
if filecheck == False:
    print('file does not exits sorry we cannot proceed')
else:
    ps = PorterStemmer() # object creation for the class for stemming the words
    CorpusFileOpen = open('E:\python programs\progrms nltk\corpus.txt','r')
    reading = CorpusFileOpen.read()
    print('Total number of characters present in the file is',len(reading))
    SentenceToken = sent_tokenize(reading)
    #for w in sent_tokenize(reading):
        #print(w)
    WordTokenize = word_tokenize(reading)
    stop_words = set(stopwords.words("english"))
    StopwordFilteredSentence = []
    #for i in word_tokenize(reading): # these two lines will tokenize the words and print one after the other
         #print(i)
     #  print(ps.stem(i))
    for word in WordTokenize:
        if word not in stop_words:
            StopwordFilteredSentence.append(word)
    print(StopwordFilteredSentence)
