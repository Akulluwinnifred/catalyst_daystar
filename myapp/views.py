from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from . forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

@login_required
def base(request):
    return render(request,'base.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            
            
            return redirect('login') 
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'change-password.html', {'form': form})


def all_babies(request):
   babies =RegisterBaby.objects.all()
   return render(request,'all_babies.html',{'babies':babies})


def babyreg(request):
   form = Babyreg_form()
   
   if request.method == 'POST':
   
      form = Babyreg_form(request.POST)
      
      if form.is_valid():
         form.save()
         messages.success(request,'Baby signed in successfully')
         return redirect('/babyreg')
   else:
      form = Babyreg_form()
      return render(request,'babyreg.html',{'form':form})
   
   
def departure(request):
    form = Departure_form()
   
    if request.method == 'POST':
   
       form = Departure_form(request.POST)
      
       if form.is_valid():
          form.save()
          messages.success(request,"Baby signed out successfully")
          return redirect('/departure')
    else:
        form = Departure_form()
    return render(request,'departure.html',{'form':form})


def read(request,id):
    babies_informations =Babyreg_form.objects.get(id=id)
    return render(request,'read.html',{'babies_informations':babies_informations})


def Sitterreg(request):
    if request.method == 'POST':
        getsitterform = Sitterreg_form(request.POST)
        if getsitterform.is_valid():
            getsitterform.save()
            messages.success(request, 'Sitter registered successfully')
            return redirect('/sitterreg')
    else:
        getsitterform = Sitterreg_form()
        return render(request, 'sitterreg.html', {'getsitterform': getsitterform})












