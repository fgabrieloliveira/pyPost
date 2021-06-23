from django.db import reset_queries
from django.shortcuts import render
from main.models import Articles
from django.conf import settings


# Create your views here.

def Index(request):
    articles_list = list()
    for articles in Articles.objects.all().order_by('-pub_date'):
        article_info = dict()
        article_info['title'] = articles.title
        article_info['headline'] = articles.headline
        article_info['pub_date'] = articles.pub_date
        article_info['id'] = articles.id
        article_info['image'] = articles.image
        

        articles_list.append(article_info)

    return render(request, 'main/dashboard.html', {'articles_list':articles_list})


def Article_datail(request, article_id):
    article_info = dict()
    article_info['title'] = Articles.objects.get(id=article_id).title
    article_info['headline'] = Articles.objects.get(id=article_id).headline
    article_info['text'] = Articles.objects.get(id=article_id).text
    article_info['author'] = Articles.objects.get(id=article_id).author
    article_info['pub_date'] = Articles.objects.get(id=article_id).pub_date
    article_info['image'] = Articles.objects.get(id=article_id).image
    

    
    

    
    return render(request, 'main/detail.html', {'article_info':article_info, 'teste':teste})


def Teste(request):
    if request.method == 'POST':
        search = str(request.POST.get('search', None)).strip().lower()
        results = list()

        for article in Articles.objects.all():
            if search in str(article.title).lower() or search in str(article.headline).lower():
                results.append(article)
    result_counter = len(results)
        
    return render(request, 'main/search.html', {'results':results, 'result_counter':result_counter})