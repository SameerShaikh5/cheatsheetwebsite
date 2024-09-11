from django.urls import path, include
from . import views


appname = 'blogs'


urlpatterns = [
    path('', views.blog, name="blogs"),
    path('<slug:slug>/', views.blogpost, name="post"),
    
]
