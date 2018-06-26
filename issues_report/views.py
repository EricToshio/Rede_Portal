from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Problem
from .forms import IssueForm, TicketForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IssueForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
            #book_inst.due_back = form.cleaned_data['renewal_date']
            #book_inst.save()
            issue = Problem(name=form.cleaned_data['name'], localization=form.cleaned_data['localization'], iniciativa=form.cleaned_data['iniciativa'],description=form.cleaned_data['description'], pub_date=timezone.now())
            issue.save()
            text = "Seu problema foi enviado com Sucesso! Para acompanhar a situação dele basta guardar o ticket:"
            response = render(request, 'issues_report/details.html', {'problem': issue, 'text': text})
            # response.delete_cookie('ticket')
            try:
                cookie_list = request.COOKIES['ticket']
            except:
                cookie_list = "[]"
            cookie_list = eval(cookie_list)
            cookie = str(issue.ticket)
            cookie_list.append(cookie)
            response.set_cookie('ticket',cookie_list,max_age=60*60*24*7) # 1 semana
            return response

        #context = {'problems_list': Problem.objects.order_by('-pub_date'),'form': form}
        #return render(request, 'issues_report/index.html', context)

    # if a GET (or any other method) we'll create a blank form
    issue_form = IssueForm()
    ticket_form = TicketForm()
    try:
        ticket_cookies = eval(request.COOKIES['ticket'])
    except:
        ticket_cookies = []
    context = {'problems_list': Problem.objects.order_by('-pub_date'),'issue_form': issue_form,'ticket_form': ticket_form, 'ticket_cookies': ticket_cookies}
    return render(request, 'issues_report/index.html', context)

def ticket(request,ticket_id=None):

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket=form.cleaned_data['ticket']
            Problem_get = get_object_or_404(Problem, ticket=ticket)
            text = "Situação do Problema: " 
            return render(request, 'issues_report/details.html', {'problem': Problem_get, 'text': text})

    Problem_get = get_object_or_404(Problem, ticket=ticket_id)
    text = "Situação do Problema: "    
    return render(request, 'issues_report/details.html', {'problem': Problem_get, 'text': text})
