import re
import os
CorpusCheck = os.path.isfile('E:\python programs\progrms nltk\corpus.txt')
if CorpusCheck == False:
    print('file does not exist sorry we cannot proceed')
else:
    FileOpen = open('E:\python programs\progrms nltk\corpus.txt','r')
    FileRead = FileOpen.read()
    numbers = re.findall(r'\d{1,9}',FileRead)
    names = re.findall(r'[A-Z][a-z]*',FileRead)

    print(numbers)
    print(names)
    print('total number of names found in the corpus is',len(names))
