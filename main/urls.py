from django.urls import path
from . import views
urlpatterns = [
path('', views.Index, name='index'),
path('article_detail/<int:article_id>', views.Article_datail, name='datail')
]