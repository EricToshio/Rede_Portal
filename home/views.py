from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from el_pagination.views import AjaxListView

from .models import News

def index(request):
    context = {'news_list_1': News.objects.order_by('-pub_date')[1:3],
               'news_list_2': News.objects.order_by('-pub_date')[3:5],
    		   'main_news': News.objects.order_by('-pub_date')[0]}
    return render(request, 'home/index.html', context)

def news_feed(request,
    template='home/news-feed-list.html',
    page_template='home/news-feed-page.html'):
    context = {
        'news_list': News.objects.order_by('-pub_date'),
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)