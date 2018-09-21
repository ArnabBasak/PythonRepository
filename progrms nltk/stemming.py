#stemming is removing the ending part of a word such as "removing has ing attach to it so stemming will remove the ing part of it "
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

#example_words = ["program","programing","programmer","programmed"]
#for w in example_words:
 #   print(ps.stem(w))
new_text = "programming is a very good subject which is dear to a programmer and today most of the things are programmed"
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))
