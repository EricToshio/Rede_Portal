from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Problem

def index(request):
    context = {'problems_list': Problem.objects.order_by('-pub_date')}
    return render(request, 'issues_report/index.html', context)
