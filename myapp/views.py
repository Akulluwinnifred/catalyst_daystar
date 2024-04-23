from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from . forms import *
from django.contrib.auth import authenticate, login
# from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy
def index(request):
    return render(request,'index.html')

# def all_babies(request):
#     return render(request,'all_babies.html')

# def all_sitters(request):
#     return render(request,'all_sitters.html')
# def babyreg(request):
#     return render(request,'babyreg.html')


# def sitterreg(request):
#     if request.method == 'POST':
#         form = Sitterreg_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('sitterreg')
#     else:
#         form=Sitterreg_form()
#     return render(request,'sitterreg.html',{'form':form}) 


# def babyreg(request):
#     if request.method == 'POST':
#         form = Babyreg_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('babyreg')
#     else:
#         form=Babyreg_form()
#     return render(request,'babyreg.html',{'form':form}) 
    

def login(request):
    return render(request,'login.html')

@login_required
def base(request):
    return render(request,'base.html')

# def signup(request):
#     if request.method == 'POST':
#         form = Signup_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('sitterreg')
#     else:
#         form=Signup_form()
#     return render(request,'signup.html', {'form':form}) 


# def arrival(request):
#     if request.method == 'POST':
#         form = Arrival_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('arrival')
#     else:
#         form=Arrival_form()
#     return render(request,'arrival.html', {'form':form})  

# def departure(request):
#     if request.method == 'POST':
#         form = Departure_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('departure')
#     else:
#         form=Departure_form()
#     return render(request,'departure.html', {'form':form})  



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
         print(form)
         return redirect('/babyreg')
   else:
      form = Babyreg_form()
#    return render(request,'all_babies.html',{'form':form})
      return render(request,'babyreg.html',{'form':form})


def read(request,id):
    babies_informations =Babyreg_form.objects.get(id=id)
    return render(request,'read.html',{'babies_informations':babies_informations})


def Sitterreg(request):
    getsitterform = Sitterreg_form()
    return render(request, 'sitterreg.html', {'getsitterform': getsitterform})


# def edit(request,id):
#    each = get_object_or_404(Babiesform,id=id)
#    if request.method == 'POST':
#       form = BabiesFormForm(request.POST,instance=each)
#       if form.is_valid():
#          form.save()
#          return redirect('/')
#    else:
#       form = BabiesFormForm(instance=each)
#    return render(request,'edit.html',{'form':form})










