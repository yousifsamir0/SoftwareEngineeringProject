from django.urls import path
from . import views

app_name = 'Groups'

urlpatterns = [


    path('Groups/<str:slug>/', views.group, name='group'),
    path('Groups/join/<str:slug>/', views.join, name='join'),
    path('Groups/cancel/<str:slug>/', views.cancelrequest, name='cancelrequest'),
    path('Groups/leave/<str:slug>/', views.leavegroup, name='leave'),
    path('Groups/accept/<str:slug>/', views.acceptreq, name='acceptreq'),
    path('Groups/refuse/<str:slug>/', views.refusereq, name='refusereq'),
    path('Groups/remmem/<str:groupslug>/',
         views.removemember, name='removemember'),


]
