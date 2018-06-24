from django.urls import path, include, re_path
from . import views

app_name = 'redecasd'
urlpatterns = [
    path('', views.index, name='index'),
    path('membros/', views.member, name='member'),
    path('membros/reservas', views.membros_reserva, name='membros_reserva'),
    path('membros/gerenciar-membros', views.membros_manage, name='membros_manage'),
    path('membros/gerenciar-membros/remover/<int:pk>', views.membros_manage_remove, name='membros_manage_remove'),
    re_path(r'^membros/gerenciar-membros/pesquisar-usuario/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.membros_manage_search, name='membros_manage_search'),
    path('membros/gerenciar-membros/adicionar/<int:pk>', views.membros_manage_add, name='membros_manage_add'),
    path('membros/reservas/<slug:modo>/<int:pk>', views.membros_reserva_positive, name='membros_reserva_positive'),
    path('reservas/', views.schedule, name='schedule'),
    path('membros/update/<int:pk>', views.problem_report_update, name='problem_report_update'),

    path('reservas/create/<slug:date>', views.reservations_create, name='reservations_create'),
    # path('reservas/update/<int:pk>', views.reservations_update, name='reservations_update'),
    path('reservas/events/', views.reservations_events, name='reservations_events'),

]