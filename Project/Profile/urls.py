from django.urls import path
from . import views

app_name = 'Profile'

urlpatterns = [
    path('myprofile/', views.myprofile, name='myprofile'),
    path('Profiles/<str:slug>/', views.profile, name='profile'),
    path('Profiles/add/<str:slug>/', views.addfriend, name='addFriend'),
    path('Profiles/cancel/<str:slug>/',
         views.cancelrequest, name='cancelRequest'),
    path('Profiles/accept/<str:slug>/',
         views.acceptrequest, name='acceptFriend'),
    path('Profiles/refuse/<str:slug>/', views.refuserequest, name='refuseFriend'),

]
