
from django.contrib import admin
from django.urls import path
from blogpost.api.views import blog_posts,blog_post

urlpatterns = [
    path('', blog_posts, name='posts'),
    path('<int:pk>', blog_post, name='post'),

]
