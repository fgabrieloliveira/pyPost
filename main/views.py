from django.shortcuts import render
from main.models import Articles

# Create your views here.

def Index(request):
    articles_list = list()
    for articles in Articles.objects.all().order_by('-pub_date'):
        article_info = dict()
        article_info['title'] = articles.title
        article_info['headline'] = articles.headline
        article_info['pub_date'] = articles.pub_date
        article_info['id'] = articles.id

        articles_list.append(article_info)

    return render(request, 'main/dashboard.html', {'articles_list':articles_list})


def Article_datail(request, article_id):
    article_info = dict()
    article_info['title'] = Articles.objects.get(id=article_id).title
    article_info['headline'] = Articles.objects.get(id=article_id).headline
    article_info['text'] = Articles.objects.get(id=article_id).text
    article_info['author'] = Articles.objects.get(id=article_id).author
    article_info['pub_date'] = Articles.objects.get(id=article_id).pub_date
    

    
    return render(request, 'main/detail.html', {'article_info':article_info})