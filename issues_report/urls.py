from django.urls import path
from . import views

app_name = 'issues_report'
urlpatterns = [
    path('', views.index, name='index'),
    path('ticket', views.ticket, name='detail_post'),
    path('ticket/<slug:ticket_id>', views.ticket, name='detail'),
]