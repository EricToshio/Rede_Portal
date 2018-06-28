from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('news-feed/', views.news_feed, name='news_feed'),
    # path('blank/', views.index_real, name='index_real'),
    path('news/', views.news, name='news'),
    path('news-manager/', views.news_manager, name='news_manager'),
    path('news-manager/create/', views.news_create, name='news_create'),
    path('news-manager/update/<int:pk>', views.news_update, name='news_update'),
    path('news-manager/remove/<int:pk>', views.news_remove, name='news_remove')
]