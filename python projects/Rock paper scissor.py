import random
print("Some Basic rules to be followed while playing the game they are: \n1.Type the word as it is mentioned in the choice of list\n2.Don't give space in the prompt")
choice = ["Rock","Paper","Scissor"]
print(computerchoice)
userchoice = input("enter your choice from \n1.Rock,\n2.Scissor\n3.Paper\n")
print("user has selected: ",userchoice)
print("computer has selected: ",computerchoice)
if computerchoice == userchoice:
    print("match drawn")
    print("Since computer has selected: ",computerchoice)
elif computerchoice > userchoice:
    print("Computer won")
    print("Since computer selected: ",computerchoice)
elif computerchoice < userchoice:
    print("Congratulation you won")
    print("Since computer selected: ",computerchoice)
else:
    print("sorry no result")
