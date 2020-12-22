from django.urls import path
from . import views

app_name = 'Profile'

urlpatterns = [
    path('myprofile/', views.myprofile,name='myprofile'),
    path('Profiles/<str:slug>/',views.profile ,name='profile'),

]
