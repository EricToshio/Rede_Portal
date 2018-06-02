from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
import simplejson

from issues_report.models import Problem
from .models import ReservationRede
from .forms import ProblemForm, ReservationForm

def index(request):
    context = {}
    print(request.COOKIES)
    return render(request, 'redecasd/index.html', context)

def schedule(request):
    context = {}
    return render(request, 'redecasd/reservas.html', context)

def member(request):
    context = {'problem_list': Problem.objects.filter(iniciativa="RedeCasd").order_by('-pub_date')}
    return render(request, 'redecasd/dashboard/index.html', context)

def membros_reserva(request):
    context = {'pedidos_de_reserva': ReservationRede.objects.filter(status="pendente")}
    return render(request, 'redecasd/dashboard/reserva-sala.html', context)

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

def reservations_events(request):
    events=get_events()
    return get_monthly_posts(events)

def reservations_create(request, date):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
    else:
        form = ReservationForm()
    context = dict()
    context['form'] = form
    context['date'] = date
    return save_reservation_form(request, context, 'redecasd/includes/partial_reservation_create.html')

def save_reservation_form(request, context, template_name):
    data = dict()
    form = context['form']
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            print("form eh valido")
        else:
            data['form_is_valid'] = False
            print("form nao eh valido")
            print(form)
    # context = {'form': form}
    form.fields['reservation_date'].initial = context['date']
    # form.fields['reservation_date'].widget = forms.HiddenInput()
    context['form'] = form
    data['html_form'] = render_to_string(template_name, context, request)
    return JsonResponse(data)

def get_monthly_posts(answer):
    return HttpResponse(simplejson.dumps(answer), content_type='application/javascript')

def get_events():
    events = []
    reservations = ReservationRede.objects.all()
    for item in reservations:
        events.append({'title':item.name, 'start': str(item.reservation_date), 'allDay': True})
    return events

