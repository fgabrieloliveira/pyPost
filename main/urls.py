from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('', views.Index, name='index'),
path('article_detail/<int:article_id>', views.Article_datail, name='datail'),
path('teste/', views.Teste, name='teste')
]
