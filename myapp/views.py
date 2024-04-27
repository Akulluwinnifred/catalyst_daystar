from django.shortcuts import get_object_or_404, render,redirect,reverse
from django.http import HttpResponse
from django.utils import timezone
from . forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *
from django.template import loader


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'access/login.html')

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
    return render(request, 'access/change-password.html', {'form': form})


def all_babies(request):
   babies =RegisterBaby.objects.all()
   return render(request,'babies/all_babies.html',{'babies':babies})


def babyreg(request):
   form = Babyreg_form()
   
   if request.method == 'POST':
   
      form = Babyreg_form(request.POST)
      
      if form.is_valid():
         form.save()
         messages.success(request,'Baby enrolled successfully')
         return redirect('/babyreg')
   else:
      form = Babyreg_form()
      return render(request,'babies/babyreg.html',{'form':form})
   

def babyarrival(request):
   form = Babyarrivalform()
   
   if request.method == 'POST':
   
      form = Babyarrivalform(request.POST)
      
      if form.is_valid():
         form.save()
         messages.success(request,'Baby signed in successfully')
         return redirect('/arrival')
   else:
      form = Babyarrivalform()
      return render(request,'babies/arrival.html',{'form':form})
   
   
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
    return render(request,'babies/departure.html',{'form':form})


def read(request,id):
    babies_informations =RegisterBaby.objects.get(id=id)
    return render(request,'babies/read.html',{'babies_informations':babies_informations})


def Sitterreg(request):
    if request.method == 'POST':
        getsitterform = Sitterreg_form(request.POST)
        if getsitterform.is_valid():
            getsitterform.save()
            messages.success(request, 'Sitter registered successfully')
            return redirect('/sitterreg')
    else:
        getsitterform = Sitterreg_form()
        return render(request, 'sitters/sitterreg.html', {'getsitterform': getsitterform})
    

def sittersattendance(request):
    if request.method == 'POST':
        form = Sittersattendance_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Sitters attendance registered successfully')
            return redirect('/tracking')
    else:
        form = Sittersattendance_form()
    return render(request, 'sitters/sittersattendance.html', {'form': form})
    

def sitters(request):
    sitters = BabySitter.objects.all()
    return render(request,'sitters/all_sitters.html',{'sitters':sitters})


def onduty(request):
    sitters = BabySitterattendance.objects.all()
    return render(request,'sitters/onduty.html',{'sitters':sitters})

def babiesdeparture(request):
    babiesdeparture = Departure.objects.all()
    return render(request,'babies/signedout.html',{'babiesdeparture':babiesdeparture})

def babysignin(request):
    babysignin = Arrivalbaby.objects.all()
    return render(request,'babies/signedin.html',{'babysignin':babysignin})

def home(request):
    # Statistics
    count_babies = RegisterBaby.objects.count()
    count_sitters = BabySitter.objects.count()
    count_departure = Departure.objects.count()
    count_arrival = Arrivalbaby.objects.count()
    count_sitterattendance = BabySitterattendance.objects.count()
    context = {
        "count_babies": count_babies,
        "count_sitters": count_sitters,
        "count_departure": count_departure,
        "count_arrival": count_arrival,
        "count_sitterattendance": count_sitterattendance,
    }
    template = loader.get_template("home.html")
    return HttpResponse(template.render(context))




def baby_edit(request, id):  
    baby = get_object_or_404(RegisterBaby, id=id)  
    if request.method == 'POST':
       form = Babyreg_form(request.POST, instance=baby)  
       if form.is_valid():
           form.save()
           return redirect(reverse('read', kwargs={'id': id})) 
    else:
        form = Babyreg_form(instance=baby)
    return render(request, 'babies/baby_edit.html', {'form': form, 'baby': baby})




