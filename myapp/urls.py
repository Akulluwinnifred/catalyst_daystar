from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),

     
     #authentication urls
    path('login/',auth_views.LoginView.as_view(template_name ='access/login.html'), name = 'login'),
    path('change-password', views.change_password, name='change-password'),
    path('home', views.home, name='home'),
    path('logout/',auth_views.LogoutView.as_view(template_name ='access/logout.html'), name = 'logout'),


       #babies urls
    path('read/<int:id>/',views.read,name='read'),
    path('all_babies/',views.all_babies,name='all_babies'),
    path("babyreg/",views.babyreg,name="babyreg"),
    path("departure/",views.departure,name="departure"),
    path("signedout/",views.babiesdeparture,name="babiesdeparture"),
    path('baby_edit/<int:id>/', views.baby_edit, name='baby_edit'),
    path('search/',views.search_babies,name='search_babies'),
    path('delete_baby/<int:baby_id>/', views.delete_baby, name='delete_baby'),

     
     #sitters urls
    path("sitterreg/",views.Sitterreg,name="sitterreg"),
    path("sitters/",views.sitters,name="sitters"),
    path("tracking/",views.sittersattendance,name="sittersattendance"),
    path("onduty/",views.onduty,name="onduty"),


    #dollscorner urls
    path('doll/',views.doll,name='doll'),
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),
    path('all_sales/',views.all_sales,name='all_sales'),
    path('issue_item/<str:pk>',views.issue_item,name='issue_item'),
    path('receipt/',views.receipt,name='receipt'),
    path('receipt_detail/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),

    #payments
    path('payment/',views.payment,name='payment'),
    path('sitterpayment/',views.sitterpayment,name='sitterpayment'),
    path('sitterpaymentlist/',views.sitterpaymentlist,name='sitterpaymentlist'),
    path('babypaymentlist/',views.babypaymentlist,name='babypaymentlist'),


    #procurement
    path('inventory/<str:pk>',views.inventory,name='inventory'),
    path('allstock/',views.allstock,name='allstock'),
    path('adding/',views.adding,name='adding'),
    path('issuing/<str:pk>',views.issuing,name='issuing'),
]



