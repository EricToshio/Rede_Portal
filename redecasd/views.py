from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group

import simplejson

from issues_report.models import Problem
from .models import ReservationRede
from .forms import ProblemForm, ReservationForm
from .helpers import redecasd_status

a="ligado"
def index(request):
    context = redecasd_status();
    print(request.COOKIES)
    return render(request, 'redecasd/index.html', context)

def schedule(request):
    context = {}
    return render(request, 'redecasd/reservas.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='RedeCasd').count() == 1, login_url='/')
def member(request):
    context = {'problem_list': Problem.objects.filter(iniciativa="RedeCasd").order_by('-pub_date')}
    return render(request, 'redecasd/dashboard/index.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='RedeCasd').count() == 1, login_url='/')
def membros_reserva(request):
    context = {'pedidos_de_reserva': ReservationRede.objects.all()}
    return render(request, 'redecasd/dashboard/reserva-sala.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='RedeCasd').count() == 1, login_url='/')
def membros_manage(request):
    context = {'membros': User.objects.filter(groups__name="RedeCasd"), 'todos_usuarios': User.objects}
    return render(request, 'redecasd/dashboard/membros-gerenciar.html', context)

def membros_manage_remove(request, pk):
    grupo_da_redecasd = Group.objects.get(name="RedeCasd")
    grupo_da_redecasd.user_set.remove(pk)
    grupo_da_redecasd.save()
    context = {'membros': User.objects.filter(groups__name="RedeCasd")}
    data ={'html_member_list': render_to_string('redecasd/includes/partial_member_manage.html', context, request)}
    return JsonResponse(data)

def membros_manage_search(request, email):
    usuarios_encontrados = User.objects.filter(email=email)
    found = len(usuarios_encontrados) != 0
    context = {'resultados': usuarios_encontrados, 'found': found, 'close_search': False }
    data ={'html_results': render_to_string('redecasd/includes/partial_member_manage_search_result.html', context, request)}
    return JsonResponse(data)

def membros_manage_add(request, pk):
    grupo_da_redecasd = Group.objects.get(name="RedeCasd")
    grupo_da_redecasd.user_set.add(pk)
    grupo_da_redecasd.save()
    context = {'membros': User.objects.filter(groups__name="RedeCasd")}
    context2 = {'resultados': None, 'found': False, 'close_search': True }
    data ={
       'html_member_list': render_to_string('redecasd/includes/partial_member_manage.html', context, request), 
       'html_results' : render_to_string('redecasd/includes/partial_member_manage_search_result.html', context2, request), 
    }
    return JsonResponse(data)

def membros_reserva_positive(request, modo, pk):
    reservation = ReservationRede.objects.get(pk=pk)
    if modo=='autorizar':
        reservation.status = 'autorizado'
    else:
        reservation.status = 'pendente'
    reservation.save()
    context = {'pedidos_de_reserva': ReservationRede.objects.all()}
    data ={'html_reservation_list': render_to_string('redecasd/includes/partial_reservations_request.html', context, request)}
    return JsonResponse(data)


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
        else:
            data['form_is_valid'] = False
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
        events.append({'title':item.name, 'start': str(item.reservation_date), 'allDay': True, 'status':item.status})
    return events

