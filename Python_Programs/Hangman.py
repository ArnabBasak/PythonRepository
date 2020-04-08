"""
The Goal: Despite the name, the actual “hangman” part isn’t necessary. The main goal here is to create a sort of “guess the word” game. The user needs to be able to input letter guesses. A limit should also be set on how many guesses they can use. This means you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list. No need to get too fancy.) You will also need functions to check if the user has actually inputted a single letter, to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.
Concepts to keep in mind:

Random
Variables
Boolean
Input and Output
Integer
Char
String
Length
Print

"""
#importing random to fetch the place and animal names randomdly
#importing textblob to do spell check  for the user input
import random
from textblob import TextBlob
class Hangman:
    def __init__(self):
        #declaring the animal features
        self.animal_dict = {
        'sounds like meow':'cat',
        'domestic animal':'dog',
        'king of jundle':'lion',
        'dangerous animal maneater':'tiger',
        'stupid animal':'donkey',
        'hardworking animal':'horse'
        }
        #declaring the place features
        self.place_dict = {
        'zero mile of india':'nagpur',
        'IT hub of india':'bangalore',
        'sweet part of india':'kolkata',
        'financial capital of india':'mumbai',
        'heart of india':'delhi',
        'dosa capital':'chennai',
        'portugues paradise':'goa',
         'queen of hills':'shimla'
        }
        #saving the dictionary list for comparision
        self.animal_list = list(self.animal_dict.values())
        self.place_list = list(self.place_dict.values())
        #declaring the score variable
        self.userscore = 0
        self.animalguess = False
        self.placeguess = False
    def userinput(self):
        #obtaining a random value from animal dictionary
        self.animal_key = random.choice(list(self.animal_dict.keys()))
        print("guess the animal who is considered ",self.animal_key)
        print()
        #asking the user to guess the animal name
        self.animal_name = input('enter your guess')
        self.animal_name = self.animal_name.lower()
        self.cleananimalname = TextBlob(self.animal_name).correct()
        print()
        #obtaining a random value from the place dictionary
        self.place_key = random.choice(list(self.place_dict.keys()))
        #asking the user to guess the place name
        print("guess the city which is considered ",self.place_key)
        print()
        self.place_name = input('enter your guess')
        #converting the user input to lower case
        self.place_name = self.place_name.lower()
        #spell checking it and correcting the input
        self.cleanplacename = TextBlob(self.place_name).correct()
    def gamePlay(self):
        if self.cleananimalname in self.animal_list:
            print('congratulation you have guessed the animal name right')
            self.animalguess = True
        if self.cleanplacename in self.place_list:
            print('congratulation you have guessed the place name right')
            self.placeguess = True
        if self.animalguess == True and self.placeguess == False:
            print('sorry you lost since you guessed the place name wrong')
        elif self.animalguess == False and self.placeguess == True:
            print('sorry you lost since you guessed the animal name wrong')
        elif self.animalguess == False and self.placeguess == False:
            print('sorry you lost since you guessed both the names wrong')
        else:
            print('congratulation you won the game')






h = Hangman()
h.userinput()
h.gamePlay()
