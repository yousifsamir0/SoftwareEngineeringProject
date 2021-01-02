from django.urls import path
from . import views

app_name = 'Posts'

urlpatterns = [
    path('postcomment/', views.postcomment, name='postcomment'),
    path('postlike/', views.likepost, name='likepost'),


]
