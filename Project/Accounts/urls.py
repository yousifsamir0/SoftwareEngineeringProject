from django.urls import path
from . import views

app_name = 'Accounts'

urlpatterns = [
    path('login/', views.login_v,name='login'),
    path('signup/',views.signup_v, name='signup' ),
    path('logout/', views.logout_v, name='logout'),


]
