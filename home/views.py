from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import News

def index(request):
    context = {'news_list': News.objects.order_by('-pub_date')[1:4],
    		   'main_news': News.objects.order_by('-pub_date')[0]}
    return render(request, 'home/index.html', context)
