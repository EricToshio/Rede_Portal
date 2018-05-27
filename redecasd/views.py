from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from issues_report.models import Problem

def index(request):
    context = {}
    return render(request, 'redecasd/index.html', context)

def member(request):
    context = {'problem_list': Problem.objects.filter(iniciativa="RedeCasd").order_by('-pub_date')}
    return render(request, 'redecasd/dashboard/index.html', context)
