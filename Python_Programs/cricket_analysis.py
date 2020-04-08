"""
In this we will analyse the batting records for the batsman
1. Plot the TOP 5 run getters
2. Plot the TOP 5 century makers
3. Plot the TOP 5 half century makers
4. Plot the TOP 5 matches palyed
5, Plot the TOP 5 innings palyed
6. Plot the TOP 5 conversion Rate
"""

import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

class analysis:
    def dataScreation(self):
        """This funtion is used for reading the html content into pandas dataframe"""
        self.data = pd.read_html('https://stats.espncricinfo.com/ci/content/records/83548.html')
        self.cricket_data = data[0]
        self.cricket_data.to_csv('batting_statistics.csv')
    def connection(self):
        """This funtion is reading the data from mysql table and creating a dataframe"""
        self.engine = create_engine('mysql+pymysql://root:library@localhost:3306/cricket')
        self.df = pd.read_sql_query('SELECT * FROM batting_statistics', self.engine)
        print(self.df.head())
    def userInterface(self):
        root = Tk()
        root.title("Cricket Analysis")
        root.geometry('400x200')
        root.resizable(0,0)
        Top5Rungetterlabel = Label(root,text="Click below to get the info for top 5 run getter in ODI cricket").grid(row=0,column=0)
        def RunGetter():
            most_runs = self.df[['Player','Runs']].head(5)
            most_runs.plot(kind='bar',x='Player',y='Runs',title='Most Runs')
            plt.xlabel("Players Name")
            plt.ylabel("Runs Scored")
            plt.show()
        Top5RunGetterButton = Button(root,text="Run Getter",command=RunGetter).grid(row=1,column=0)
        root.mainloop()

a = analysis()
a.connection()
a.userInterface()



"""    import mysql.connector as sql

    import pandas as pd

    db_connection = sql.connect(host='hostname', database='db_name', user='username', password='password')

    db_cursor = db_connection.cursor()

    db_cursor.execute('SELECT * FROM table_name')

    table_rows = db_cursor.fetchall()

    df = pd.DataFrame(table_rows)
"""
