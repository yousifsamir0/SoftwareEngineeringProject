from django.urls import path
from . import views


app_name = 'Posts'

urlpatterns = [
    path('postcomment/', views.postcomment, name='postcomment'),
    path('postlike/', views.likepost, name='likepost'),
    path('postsave/', views.savepost, name='savepost'),
    path('newPost/<str:slug>/', views.grouppost, name='grouppost'),
    path('pPost/', views.ppost, name='ppost'),
    path('hPost/', views.hpost, name='hpost'),


]
