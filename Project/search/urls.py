from django.urls import path
from . import views


app_name = 'search'

urlpatterns = [

    path('search/', views.search_view, name='search'),
    path('search/<str:query>/', views.searchpage, name='searchpage'),


]
