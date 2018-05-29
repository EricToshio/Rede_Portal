from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse

from issues_report.models import Problem
from .forms import ProblemForm

def index(request):
    context = {}
    return render(request, 'redecasd/index.html', context)

def member(request):
    context = {'problem_list': Problem.objects.filter(iniciativa="RedeCasd").order_by('-pub_date')}
    return render(request, 'redecasd/dashboard/index.html', context)

def problem_report_update(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == 'POST':
        form = ProblemForm(request.POST, instance=problem)
    else:
        form = ProblemForm(instance=problem)
    return save_problem_form(request, form, 'redecasd/includes/partial_report_problem_update.html')

def save_problem_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            problems = Problem.objects.filter(iniciativa="RedeCasd").order_by('-pub_date')
            data['html_problem_list'] = render_to_string('redecasd/includes/partial_report_problem_list.html', {
                'problem_list': problems
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request)
    return JsonResponse(data)


