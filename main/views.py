from django.db import reset_queries
from django.shortcuts import render
from main.models import Articles
from django.conf import settings


# Create your views here.

def Index(request):
    articles = list()
    for article in Articles.objects.all().order_by('-pub_date'):
        
        articles.append(article)

    return render(request, 'main/dashboard.html', {'articles':articles})


def Article_datail(request, article_id):
    article = Articles.objects.get(id=article_id)
    
    return render(request, 'main/detail.html', {'article':article})


def Teste(request):
    if request.method == 'POST':
        search = str(request.POST.get('search', None)).strip().lower()
        results = list()

        for article in Articles.objects.all():
            if search in str(article.title).lower() or search in str(article.headline).lower():
                results.append(article)
    result_counter = len(results)
        
    return render(request, 'main/search.html', {'results':results, 'result_counter':result_counter})