from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    # path('blank/', views.index_real, name='index_real'),
]