from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('news-feed/', views.news_feed, name='news_feed'),
    # path('blank/', views.index_real, name='index_real'),
    path('news/', views.news, name='news')
]