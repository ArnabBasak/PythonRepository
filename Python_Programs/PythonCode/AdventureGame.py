"""
The Goal: Remember Adventure? Well, we’re going to build a more basic version of that.
 A complete text game, the program will let users move through rooms based on user input and get descriptions of each room.
 To create this, you’ll need to establish the directions in which the user can move,
 a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description.
 You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user,
  “You can’t move further in this direction.”
Concepts to keep in mind:

Strings
Variables
Input/Output
If/Else Statements
Print
List
Integers


The tricky parts here will involve setting up the directions and keeping track of just how far the user has “walked” in the game.
 I suggest sticking to just a few basic descriptions or rooms, perhaps 6 at most.
 This project also continues to build on using userinputted data.
 It can be a relatively basic game, but if you want to build this into a vast, complex word,
 the coding will get substantially harder, especially if you want your user to start interacting with actual objects within the game.
 That complexity could be great, if you’d like to make this into a longterm project. *Hint hint.

"""

class AdventureGame:
    def __init__(self):
        self.house_one = 1
        self.house_two = 2
        self.house_three = 3
        self.house_four = 4
        self.house_five = 5
        self.house_six = 6
        self.rooms_house_one = ["Bedroom","Hall","Kitchen"]
        self.rooms_house_two = ["MasterBedroom","Bedroom","Hall","Kitchen"]
        self.rooms_house_three = ["MasterBedroom","Guestroom1","Guestroom2","Hall","Kitchen"]
        self.rooms_house_four = ["MasterBedroom","Guestroom1","Guestroom2","Guestroom3","Hall","Kitchen"]
        self.rooms_house_five = ["MasterBedroom","Guestroom1","Guestroom2","Guestroom3","Guestroom4","Hall","Kitchen"]
        self.rooms_house_six = ["MasterBedroom","Guestroom1","Guestroom2","Guestroom3","Guestroom4","Guestroom5","Hall","Kitchen"]
        self.description = {
        'Bedroom' : 'This is a space having arrengment for the house owner to sleep',
        'MasterBedroom' : 'This is space having arrengment for the house owner to sleep',
        'Hall' : 'This is space where the living space is designed',
        'Kitchen' : 'This is a space where cooking arrengments are made',
        'Guestroom' : 'This space is designed for the guests to stay'
        }
        self.score = 0
    def userinput(self):
        print("Press 1 for House one")
        print("Press 2 for House two")
        print("Press 3 for House three")
        print("Press 4 for House four")
        print("Press 5 for House five")
        print("Press 6 for House six")
        print()
        self.userchoice = int(input('Select from above option where do you want to enter'))
        print()
        if self.userchoice not in range(1,6):
            print("invalid option please enter again")
            self.userinput()
    def gamePlay(self):
            print("================================")
            print("Press B for Bedroom")
            print("Press M for MasterBedroom")
            print("Press H for Hall")
            print("Press K for Kitchen")
            print("Press G for Guestroom")
            print("================================")
            print()
            self.userroom = input('What do you think where did you entered choose from the above options')
            print()
            self.userdiscription = input('enter your discription for the room')
            if self.userroom == 'B':
                self.discriptiondata = self.description.get("Bedroom","")
                self.score += 1
            elif self.userroom == 'M':
                self.discriptiondata = self.description.get("MasterBedroom","")
                self.score  += 1
            elif self.userroom == 'H':
                self.discriptiondata = self.description.get("Hall","")
                self.score += 1
            elif self.userroom == 'K':
                self.discriptiondata = self.description.get("Kitchen","")
                self.score += 1
            elif self.userroom == 'G':
                print("Sorry there is no such room")
                self.score -= 1
            else:
                print("Sorry invalid option")
    def Play(self):
            if self.userchoice == 1:
                print("YOU CHOOSE TO ENTER IN HOUSE 1 WHICH COMPRISES OF 3 ROOMS IN TOTAL")
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                print("your final score is",self.score)
            elif self.userchoice == 2:
                print('YOU CHOOSE TO ENTER IN HOUSE 2 WHICH COMPRISES OF 4 ROOMS IN TOTAL')
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                print('Your final score is',self.score)
            elif self.userchoice == 3:
                print('YOU CHOOSE TO ENTER IN HOUSE 3 WHICH COMPRISES OF 5 ROOMS IN TOTAL')
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                print('Your final score is',self.score)
            elif self.userchoice == 4:
                print('YOU CHOOSE TO ENTER IN HOUSE 4 WHICH COMPRISES OF 6 ROOMS IN TOTAL')
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                print('Your final score is',self.score)
            elif self.userchoice == 5:
                print('YOU CHOOSE TO ENTER IN HOUSE 4 WHICH COMPRISES OF 7 ROOMS IN TOTAL')
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                print('Your final score is',self.score)
            elif self.userchoice == 6:
                print('YOU CHOOSE TO ENTER IN HOUSE 4 WHICH COMPRISES OF 8 ROOMS IN TOTAL')
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                self.gamePlay()
                print('Your final score is',self.score)
            else:
                print('Please select a proper option')






Ag = AdventureGame()
Ag.userinput()
Ag.gamePlay()
Ag.Play()
