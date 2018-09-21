import nltk
from nltk.tokenize import PunktSentenceTokenizer
sample_text = "Arnab Basak is starting to find his foot in nltk with the help of sentdex and he is also interested in Sachin and cricket"
sentencetokenizer = PunktSentenceTokenizer(sample_text)
tokenized = sentencetokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

process_content()
