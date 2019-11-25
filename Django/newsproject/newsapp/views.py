# importing api
from django.shortcuts import render
from newsapi import NewsApiClient
from django.http import HttpResponse

# Create your views here.
def index(request):

	newsapi = NewsApiClient(api_key ='f1c1a3571dfb4ad2a7c3d476485a7728')
	top = newsapi.get_top_headlines(sources ='techcrunch')

	l = top['articles']
	desc =[]
	news =[]
	img =[]

	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)

	return render(request, 'index.html', context ={"mylist":mylist})