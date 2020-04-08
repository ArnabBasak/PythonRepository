import tkinter as tk
from tkinter import messagebox
from tkinter import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
root = tk.Tk()
#This set the name for the window
root.title('Sentiment analyzer')
#set set the default size of the window
root.geometry('800x200')
#this stops the window from getting maximized
root.resizable(0,0)
#This is setting the labbels
label = tk.Label(root,text='Sentiment analysis for the social media platform').grid(row=0,column=2)
statusLabel = tk.Label(root,text="Enter your status",).grid(row=2,column=1)
#This is setting the entry widget
statusEntry = tk.Entry(root,width=100)
statusEntry.grid(row=2,column=2,ipady=20)
#setting the radio button
radio = IntVar()
VaderSentiment = tk.Radiobutton(root,text="Vader Setiment",variable=radio,value=0).grid(row=3,column=2)
NltkSentiment = tk.Radiobutton(root,text="NLTK Setiment",variable=radio,value=1).grid(row=4,column=2)
#initializing the sentiment analyzer
obj = SentimentIntensityAnalyzer()
def SentumentCalculation():
    selection = str(radio.get())
    status = statusEntry.get()
    if len(status) == 0:
        messagebox.showinfo('warning',"Please enter the status")
    else:
        if selection == '0' : #vader sentiment
            sentiment_dict = obj.polarity_scores(status)
            if sentiment_dict['compound'] >= 0.05:
                messagebox.showinfo("Sentiment","Status is positive")
            elif sentiment_dict['compound'] <= -0.05:
                messagebox.showinfo("Sentiment","Status is Negative")
            else:
                messagebox.showinfo("Sentiment","Status is neutral")
        elif selection == '1': #NLTK Sentiment
            analysis = TextBlob(status)
            if analysis.sentiment.polarity > 0:
                messagebox.showinfo('Sentiment',"Status is positive")
            elif analysis.sentiment.polarity == 0:
                messagebox.showinfo('Sentiment',"Status is neutral")
            else:
                messagebox.showinfo('Sentiment',"Status is negative")
        else:
            messagebox.showinfo('answer',status)


#This is setting the button
check = tk.Button(root,text="Check Status",command=SentumentCalculation).grid(row=5,column=2,padx=10,pady=10)
#This is packing all the widgets in the loop
root.mainloop()
