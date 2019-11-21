""" import nltk
nltk.download() """
import string
mystring = "this is ....... a string !!! creaated by me..{"
removedstring = mystring.translate(string.punctuation)
print(removedstring)