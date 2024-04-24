from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('login/',auth_views.LoginView.as_view(template_name ='login.html'), name = 'login'),
    path('change-password', views.change_password, name='change-password'),
    path('read/<int:id>/',views.read,name='read'),
    path('all_babies/',views.all_babies,name='all_babies'),
    path("babyreg/",views.babyreg,name="babyreg"),
    path("sitterreg/",views.Sitterreg,name="sitterreg"),
    path("read/",views.read,name="read"),
    path("departure/",views.departure,name="departure"),
    path('logout/',auth_views.LogoutView.as_view(template_name ='logout.html'), name = 'logout'),
     
]



