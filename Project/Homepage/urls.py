from django.urls import path
from . import views

app_name = 'Homepage'

urlpatterns = [
    path('', views.Home, name='homepage'),
    path('saved/', views.savedposts, name='savedposts'),

]
