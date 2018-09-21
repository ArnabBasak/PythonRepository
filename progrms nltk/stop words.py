from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "this is a first sentence written by me in the nltk python."
stop_words = set(stopwords.words("english"))
print('original sentence is',example_sentence)
#print(stop_words)
words = word_tokenize(example_sentence)
filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)
#it can be done in one line as well
filtered_sentence1 = [w for w in words if not w in stop_words]
print(filtered_sentence1)
#stop words are the punctuation words which are used in the english sentence such as "is an etc"
