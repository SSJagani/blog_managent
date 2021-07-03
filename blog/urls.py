from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('postComment' ,views.blogComment ,name='BlogComment'),
    
    path('', views.index,name='BlogHome'),
    path('<str:slug>/', views.blogpost,name='BlogPost'),

]