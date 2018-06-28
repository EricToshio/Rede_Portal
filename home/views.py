from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from el_pagination.views import AjaxListView
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import News
from .forms import NewsForm

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

def news(request):
    id_parameter = request.GET['toshio_pistola']
    context = {'news': News.objects.filter(id=id_parameter)[0]}
    return render(request, 'home/news.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='CASD').count() == 1, login_url='/')
def news_manager(request):
    context = {
        'news_list': News.objects.order_by('-pub_date')
    }
    return render(request, 'home/manager/news-manager.html', context)

def news_create(request):
    form = NewsForm(request.POST or None)

    if form.is_valid():
        form.save()        
    else:
        form = NewsForm()

    context = {
        'form': form,
    }
    return render(request, 'home/manager/news-add.html', context)

def news_remove(request, pk):
    news = get_object_or_404(News, pk=pk)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        news.delete()
    else:
        form = NewsForm(instance=news)

    context = {
        'form': form,
    }
    return render(request, 'home/manager/news-edit.html', context)

def news_update(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
    else:
        form = NewsForm(instance=news)

    context = {
        'form': form,
    }
    return save_news_form(request, 'home/manager/news-edit.html', context)

def save_news_form(request, template_name, form):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            problems = Problem.objects.filter(iniciativa="RedeCasd").order_by('-pub_date')
            data['html_problem_list'] = render_to_string('home/manager/news_list.html', {
                'problem_list': problems
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request)
    return JsonResponse(data)