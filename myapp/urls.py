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
    path('logout/',auth_views.LogoutView.as_view(template_name ='logout.html'), name = 'logout'),
     
]



# from django.urls import path
# from . import views 
# from django.contrib.auth import views as auth_views
# from .views import CustomPasswordResetView, CustomPasswordResetDoneView

# urlpatterns = [
    #  path("",views.index,name='index'),
#     path('login/',auth_views.LoginView.as_view(template_name ='login.html'), name = 'login'),
#     path('logout/',auth_views.LogoutView.as_view(template_name ='logout.html'), name = 'logout'),
#     path('all_babies/',views.all_babies,name='all_babies'),
#     path('all_sitters/',views.all_sitters,name='all_sitters'),
#     path('sitterreg/',views.sitterreg,name='sitterreg'),
#     path("signup/",views.signup,name= "signup"),
#     path("babyreg/",views.babyreg,name="babyreg"),
#     path("base/",views.base,name="base"),
#     path("arrival/",views.arrival,name="arrival"),
#     path("departure/",views.departure,name="departure"),
#     path('change-password', views.change_password, name='change-password'),
    
#     path('password_reset/',views.CustomPasswordResetView.as_view(), name = 'password_reset'),
#     path('password_reset_done/',CustomPasswordResetDoneView.as_view(), name = 'password_reset_done'),
#     path('password_reset_confirm/<slug:uidb64>/<slug:token>/',auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
#     path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')

# ]