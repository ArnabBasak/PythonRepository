import pandas as pd 
from pandasql import sqldf
#from requests import get
usermovie_dataframe = pd.read_csv('mymovielist.csv')
#print(type(usermovie_dataframe))
#url = "https://www.imdb.com/india/top-rated-indian-movies/"
#response = get(url)
#print(response.text[:500])
#print(usermovie_dataframe["rating"].mean())
