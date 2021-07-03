from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index,name='Home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('search/', views.search,name='search'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout,name='logout'),
    path('map/', views.map,name='map'),
]