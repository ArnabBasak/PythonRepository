# python programs to remove puncutatuon marks
punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_string = input("enter any string with punctuation")
no_punct =""
for i in my_string:
    if i not in punctuation:
        no_punct = no_punct+i
print(no_punct)