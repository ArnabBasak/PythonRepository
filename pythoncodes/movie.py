import numpy as np
import math
#this is the static data 
moviedictionary = {
    "Anand":8.7,
    "Drishyam":8.6,
    "Golmal":8.5,
    "Black Friday":8.5,
    "Dangal":8.4,
    "Taare Zameen Par":8.4,
    "Pather Panchali":8.4,
    "3 ediots":8.4,
    "Chupke Chupke":8.4,
    "Guide":8.3
    }
#print(moviedictionary)
#this variable is to insert the users movie list
usermovielist = []
# if the movie is not present in the static data
newmovielist = []
#declaring the range
poorlist = (np.arange(0,4,0.1))
averagelist = (np.arange(4,6,0.1))
aboveaveragelist = (np.arange(6,8,0.1))
excellentlist = (np.arange(8,10,0.1))
#inserting the movie names
usersmovie1 = input("Enter the 1st movie name you watched\n")
if usersmovie1 in moviedictionary:
    usermovielist.append(moviedictionary[usersmovie1])
else:
    print('since this movie is not in our list we will be adding it in our list')
    newmovielist.append(usersmovie1)
usersmovie2 = input("Enter the 2nd movie name you watched\n")
if usersmovie2 in moviedictionary:
    usermovielist.append(moviedictionary[usersmovie2])
else:
    print('since this movie is not in our list we will be adding it in our list')
    newmovielist.append(usersmovie2)
usersmovie3 = input("Enter the 3rd movie name you watched\n")
if usersmovie3 in moviedictionary:
    usermovielist.append(moviedictionary[usersmovie3])
else:
    print('since this movie is not in our list we will be adding it in our list')
    newmovielist.append(usersmovie3)
usersmovie4 = input("Enter the 4th movie name you watched\n")
if usersmovie4 in moviedictionary:
    usermovielist.append(moviedictionary[usersmovie4])
else:
    print('since this movie is not in our list we will be adding it in our list')
    newmovielist.append(usersmovie4)
usersmovie5 = input("Enter the 5th movie name you watched\n")
if usersmovie5 in moviedictionary:
    usermovielist.append(moviedictionary[usersmovie5])
else:
    print('since this movie is not in our list we will be adding it in our list')
    newmovielist.append(usersmovie5)
#calculating the mean for the users rating
usermean = np.mean(usermovielist)
roundingoff = math.floor(usermean)
print(newmovielist)
if roundingoff in poorlist:
    print('user likes generally movies with poor ratings')
if roundingoff in averagelist:
    print('user likes generally movies with average ratings')
if roundingoff in aboveaveragelist:
    print('user likes generally movies with above ratings')
if roundingoff in excellentlist:
    print('user likes generally movies with execellent ratings')
print('users average movie watching rating is ',usermean)






