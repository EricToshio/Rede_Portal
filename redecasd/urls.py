from django.urls import path, include
from . import views

app_name = 'redecasd'
urlpatterns = [
    path('', views.index, name='index'),
    path('membros/', views.member, name='member'),
]