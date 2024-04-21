from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from . forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.template.loader import render_to_string
# from django.core.mail import send_mail
# from django.contrib.sites.shortcuts import get_current_site
# # Create your views here.
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
   return render(request,'babyreg.html',{'form':form})
   if request.method == 'POST':
   
      form = Babyreg_form(request.POST)
      
      if form.is_valid():
         form.save()
         print(form)
         return redirect('/babyreg')
   else:
      form = Babyreg_form()
   return render(request,'all_babies.html',{'form':form})


def read(request,id):
    babies_informations =Babyreg_form.objects.get(id=id)
    return render(request,'read.html',{'babies_informations':babies_informations})


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






# # views.py

# class CustomPasswordResetView(PasswordResetView):
#     email_template_name = 'password_reset_email.html'
#     template_name = 'password_reset_form.html'
#     success_url = '/password_reset_done/'

# class CustomPasswordResetDoneView(PasswordResetDoneView):
#     template_name = 'password_reset_done.html'


def password_reset_email(request):
    context = {
        'protocol': 'https',
        'domain': 'example.com',
        'uid': 'user_id',
        'token': 'reset_token',
        'timeout': 24,
    }
    return render(request, context)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
