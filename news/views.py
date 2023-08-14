from django.shortcuts import render
import requests
import random

def index(request):
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-04-13&sortBy=publishedAt&apiKey=dc727b929b5b44aaac37fd5436c577b3'
    news_data = []
    response = requests.get(url).json()
    image_urls = [
    "https://images.pexels.com/photos/2380451/pexels-photo-2380451.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://images.pexels.com/photos/1029618/pexels-photo-1029618.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    "https://images.pexels.com/photos/1557238/pexels-photo-1557238.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    "https://images.pexels.com/photos/7078717/pexels-photo-7078717.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://images.pexels.com/photos/6476117/pexels-photo-6476117.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://static.vecteezy.com/system/resources/previews/007/188/453/original/abstract-blur-background-with-pastel-color-free-vector.jpg",
    "https://images.pexels.com/photos/7232394/pexels-photo-7232394.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    "https://images.pexels.com/photos/7078622/pexels-photo-7078622.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    ]
    
    for i in range(30):
        article = response['articles'][i]
        
        # Assign a different pastel image URL to each article
        news = {
            'title': article['title'],
            'description': article['description'],
            'source': article['source']['name'],
            'url': article['url'],
              # Assign a different pastel image to each article
        }
        
        news_data.append(news)
        
    context = {'news_data': news_data, 'image_urls': image_urls,}
    
    return render(request, 'news/index.html', context)
