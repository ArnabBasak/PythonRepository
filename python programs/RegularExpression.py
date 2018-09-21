'''
Identifiers:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. any character,except for a newline
\b the whitespace around words
\. a period

Modifiers:
{1,3} we are expecting 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ matching the beginning of a string
| either or
[] range or "variance" [A +Z]
{x} expecting "x" amount

White
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

DONT FORGET!:
. + * ? [ ] $ ^ ( ) { } | \
'''

import re
exampleString ='''hello Arnab is 24
Roshni is also 24 and
Pranay is 24 as well'''
print('this is the sample string',exampleString)

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

ageDict = {}

x = 0
for eachName in names:
    print(eachName)
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)

