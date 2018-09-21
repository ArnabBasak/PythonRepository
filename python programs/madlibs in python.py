# program to code a game called madlibs
playername = input('enter your name')
print("Hello\n",playername,"follow the prompt to play the game: ")
proper_name1 = input("Enter a name: ")
proper_name2 = input("Enter another name: ")
noun1 = input("Enter a proper title: ")
place1 = input("Enter a place: ")
place2 = input("Enter another place: ")
verb1 = input("Enter a present-tense verb: ")
noun3 = input("Enter a noun: ")
noun2 = input("Enter a plural noun: ")
noun4 = input("Enter another plural noun: ")
num2 = input("Enter a number: ")
num1 = input("Enter another number: ")
percent1 = input("Enter another number: ")

print("Dear {}, It is my pleasure to {} to you today. I am {} and I'm the "
      "{} of {}. I have inherited {} {} but I need your help to get it to {}. "
      "Please send me your {} and the sum of {} {} to get started, and I will "
      "give you {} percent of my inheritance. Yours truly, {}".format(
          proper_name1, verb1, proper_name2, noun1, place1, num1, noun2,
          place2, noun3, num2, noun4, percent1, proper_name2))