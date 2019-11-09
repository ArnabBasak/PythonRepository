from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import operator
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize,word_tokenize

def home(request):
        usertext = request.GET['text']
        if len(usertext) == 0:
            return render(request,'login.html')
        else:
            if datetime.now().hour > 12:
                return render(request,'home.html',{'greetings':'Good evening','welcome':usertext})
            else:
                return render(request,'home.html',{'greetings':'Good morning','welcome':usertext})

def count(request):
    return render(request,'count.html')

def result(request):
    fulltext = request.GET['fulltext']
    if len(fulltext) == 0:
        return render(request,'resultcount.html',{'fulltext':'','count':len(fulltext)})
    else:
        wordlist = fulltext.split()
        worddictionary = {}
        for word in wordlist:
            if word in worddictionary:
                worddictionary[word] += 1
            else:
                worddictionary[word] = 1
        sortedwords =  sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
        return render(request,'resultcount.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')

def textblob(request):
    return render(request,'textblob.html')

def textblobresult(request):
    sentimenttext = request.GET['sentimenttext']
    if len(sentimenttext) == 0:
        return render(request,'textblob.html')
    else:
        analysis = TextBlob(sentimenttext)
        score = analysis.sentiment.polarity
        if score > 0:
            return render(request,'textblobresult.html',{'sentence':sentimenttext,'output':'sentence is positive','score':score})
        elif score  == 0:
            return render(request,'textblobresult.html',{'sentence':sentimenttext,'output':'sentence is neutral','score':score})
        else:
            return render(request,'textblobresult.html',{'sentence':sentimenttext,'output':'sentence is negative','score':score})

def vader(request):
        return render(request,'vader.html')

def vaderresult(request):
    sentimenttext = request.GET['sentimenttext']
    if len(sentimenttext) == 0:
        return render(request,'vader.html')
    else:
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(sentimenttext)
        neg_per = sentiment_dict['neg']*100
        pos_per = sentiment_dict['pos']*100
        neu_per = sentiment_dict['neu']*100
        if sentiment_dict['compound'] >= 0.05:
            overall = 'Positive'
        elif sentiment_dict['compound'] <= -0.05:
            overall = 'Negative'
        else:
            overall = 'Neutral'
        return render(request,'vaderresult.html',{'sentence':sentimenttext,'output':sentiment_dict,'neg_per':neg_per,'pos_per':pos_per,'neu_per':neu_per,'overall':overall})

def login(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')
def token(request):
    return render(request,'token.html')
def tokenresult(request):
    tokentext = request.GET['tokentext']
    if len(tokentext) == 0:
        return render(request,'token.html')
    else:
        senttoken = sent_tokenize(tokentext)
        wordtoken = word_tokenize(tokentext)
        return render(request,'tokenresult.html',{'sentence':tokentext,'wordtoken':wordtoken,'senttoken':senttoken})
