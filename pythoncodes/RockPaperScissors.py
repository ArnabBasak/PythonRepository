"""Python program for Rock Paper Scissors"""
import datetime
import random
Playername = input('Enter your name\n')
"""this statement is comparing the current time with 12 o clock that is the mid day """
if datetime.datetime.now().time() <= datetime.datetime.now().time().replace(hour = 12,minute = 0,second = 0,microsecond = 0):
    print('Hello\n',"Good Morning",Playername)
else:
    print('Hello\n',"Good Evening",Playername)
choicelist = ['Rock','Paper','Scissors']
#print(random.choice(gamelist))
print('1 player game','or','2 Player game','Enter your choice\n')
Playerselection = int(input())
if Playerselection == 1:
    Playerchoice = input('Enter your choice\n')
    if Playerchoice ==  'Rock' and random.choice(choicelist) == 'Rock':
        print('Its a tie')
    elif Playerchoice == 'Rock' and random.choice(choicelist) == 'Paper':
        print(Playername,'Lose paper covers rock')
    elif Playerchoice == 'Rock' and random.choice(choicelist) == 'Scissors':
        print(Playername,'Won Congratulations Rock smashes Scissors')
    elif Playerchoice ==  'Paper' and random.choice(choicelist) == 'Rock':
        print(Playername,'Won Congratulation paper covers rock')
    elif Playerchoice == 'Paper' and random.choice(choicelist) == 'Paper':
        print('Its a tie both of the player selected papers')
    elif Playerchoice == 'Paper' and random.choice(choicelist) == 'Scissors':
        print(Playername,'Lose Scissors cuts the paper')
    elif Playerchoice ==  'Scissors' and random.choice(choicelist) == 'Rock':
        print(Playername,'Lose Rock smashes Scissors')
    elif Playerchoice == 'Scissors' and random.choice(choicelist) == 'Paper':
        print(Playername,'Won scissors cut paper')
    elif Playerchoice == 'Scissors' and random.choice(choicelist) == 'Scissors':
        print('Its a tie both the players selected Scissors')
    else:
        print('Please select a proper option')
elif Playerselection == 2:
    Player2name = input('enter second player name')
    Player1Choice = input('Player 1 Enter your choice\n')
    Player2Choice = input('Player 2 Enter your choice\n')
    if Player1Choice == 'Rock' and Player2Choice == 'Rock':
        print('its a tie Both the players selected rock')
    elif Player1Choice == 'Paper' and Player2Choice == 'Rock':
        print(Playername,'Won congratulation paper covers Rock')
    elif Player1Choice == 'Scissors' and Player2Choice =='Rock':
        print(Player2name,'Won congratulation Rock Smashes Scissors')
    elif Player1Choice == 'Rock' and Player2Choice == 'Paper':
        print(Player2name,'Won congratulation Paper covers rock')
    elif Player1Choice == 'Paper' and Player2Choice == 'Paper':
        print('Its a tie both the players selected papers')
    elif Player1Choice == 'Scissors' and Player2Choice =='Paper':
        print(Playername,'Won congratulation Scissors cut paper ')
    elif Player1Choice == 'Rock' and Player2Choice == 'Scissors':
        print(Playername,'Won congratulation Rock smashes scissors')
    elif Player1Choice == 'Paper' and Player2Choice == 'Scissors':
        print(Player2name,'won congratulation Scissors cut paper')
    elif Player1Choice == 'Scissors' and Player2Choice =='Scissors':
        print('its a tie both players selected Scissors')
    else:
        print('please select a proper option to play')        
else:
    print('Please select a proper option to play')
