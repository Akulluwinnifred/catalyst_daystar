from django.shortcuts import get_object_or_404, render,redirect,reverse
from django.http import HttpResponse
from django.utils import timezone
from . forms import *
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *
from django.template import loader


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'access/login.html')


def logout(request):
    return render(request,'access/logout.html')

@login_required
def base(request):
    return render(request,'base.html')

@login_required
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

@login_required
def all_babies(request):
   babies =RegisterBaby.objects.all()
   return render(request,'babies/all_babies.html',{'babies':babies})

@login_required
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
   

# def babypayment(request):
#    form = Payment_form()
   
#    if request.method == 'POST':
   
#       form = Payment_form(request.POST)
      
#       if form.is_valid():
#          form.save()
#          messages.success(request,'Payment registered successfully')
#          return redirect('/babypayment')
#    else:
#       form = Payment_form()
#       return render(request,'baby_payments/babypayment.html',{'form':form})

@login_required
def babypayment(request):
    form = Payment_form()
   
    if request.method == 'POST':
   
       form = Payment_form(request.POST)
      
       if form.is_valid():
          form.save()
          messages.success(request,"Baby signed out successfully")
          return redirect('/babypayment')
    else:
        form = Payment_form()
    return render(request,'baby_payments/babypayment.html',{'form':form})


@login_required
def babyarrival(request):
    if request.method == 'POST':
        form = Babyarrivalform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Baby signed in successfully')
            return redirect('/arrival')
        else:
            messages.error(request, 'Form submission failed. Please check the data entered.')
            # If the form is not valid, re-render the form with validation errors
            return render(request, 'babies/arrival.html', {'form': form})
    else:
        # If the request method is not POST, create a new form instance and render the form
        form = Babyarrivalform()
        return render(request, 'babies/arrival.html', {'form': form})
   

@login_required
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


@login_required
def read(request,id):
    babies_informations =RegisterBaby.objects.get(id=id)
    return render(request,'babies/read.html',{'babies_informations':babies_informations})


@login_required
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


@login_required
# def assign(request):
#     if request.method == 'POST':
#         form = Assignbabies_form(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Sitter assigned successfully')
#             return redirect('/assign')
#     else:
#         form = Assignbabies_form()
#     return render(request, 'babies/assign.html', {'form':form})
    

# def assign(request):
#     if request.method == 'POST':
#         form = Assignbabies_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('assignedsitter')
#     else:
#         # Get the list of arrived sitters and babies
#         arrived_sitters = BabySitterattendance.objects.all()
#         arrived_babies = Arrivalbaby.objects.all()
#         form = Assignbabies_form()
#         form.fields['sitter_name'].queryset = arrived_sitters
#         form.fields['baby_name'].queryset = arrived_babies
#     return render(request, 'babies/assign.html', {'form': form})


@login_required
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
    

@login_required
def sitters(request):
    sitters = BabySitter.objects.all()
    return render(request,'sitters/all_sitters.html',{'sitters':sitters})

# @login_required
# def assignedsitter(request):
#     babies = Assignbabies.objects.all()
#     return render(request,'babies/assignedsitters.html',{'babies':babies})


@login_required
def onduty(request):
    sitters = BabySitterattendance.objects.all()
    return render(request,'sitters/onduty.html',{'sitters':sitters})


@login_required
def babiesdeparture(request):
    babiesdeparture = Departure.objects.all()
    return render(request,'babies/signedout.html',{'babiesdeparture':babiesdeparture})


@login_required
def babysignin(request):
    babysignin = Arrivalbaby.objects.all()
    return render(request,'babies/signedin.html',{'babysignin':babysignin})


@login_required
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


@login_required
def search_babies(request):
    query = request.GET.get('search_query')
    baby_list = RegisterBaby.objects.filter(name__contains=query)
    return render(request,'babies/all_babies.html',{'baby_list':baby_list,'search_query':query})



@login_required
def baby_edit(request, id):  
    baby = get_object_or_404(RegisterBaby, id=id)  
    if request.method == 'POST':
       form = Babyreg_form(request.POST, instance=baby)  
       if form.is_valid():
           form.save()
           return redirect(all_babies) 
    else:
        form = Babyreg_form(instance=baby)
    return render(request, 'babies/baby_edit.html', {'form': form, 'baby': baby})



@login_required
def receipt(request):
    sales= Salesrecord.objects.all().order_by('-id') 
    return render(request,'dolls/receipt.html',{'sales':sales})  


@login_required
def issue_item(request,pk):
    issued_item=Doll.objects.get(id=pk) 
    sales_form=SalesrecordForm(request.POST)  

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale=sales_form.save(commit=False)
            new_sale.doll=issued_item
            new_sale.unit_price=issued_item.Unit_price
            new_sale.save()
            issued_quantity=int(request.POST['quantity_sold'])
            issued_item.quantity-=issued_quantity
            issued_item.save()
            print(issued_item.name_of_the_doll)
            print(request.POST['quantity_sold'])
            print(issued_item.quantity)
            return redirect('receipt')
    return render(request, 'dolls/issue_item.html',{'sales_form':sales_form} )

@login_required
def receipt_detail(request, receipt_id):
            receipt = Salesrecord.objects.get(id=receipt_id)
            return render(request,'dolls/receipt_detail.html',{'receipt':receipt})

@login_required
def add_to_stock(request,pk):
    issued_item=Doll.objects.get(id=pk)
    form=Addform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            added_quantity=int(request.POST['received_quantity'])
            issued_item.quantity+=added_quantity
            issued_item.save()
            print(added_quantity)
            print(issued_item.quantity)
            return redirect('doll')
    return render(request, 'dolls/add_to_stock.html',{'form':form})

@login_required
def all_sales(request):
    sales=Salesrecord.objects.all()
    total=sum([items.amount_received for items in sales])
    change=sum([items.get_change() for items in sales])
    net=total-change
    return render(request,'dolls/all_sales.html',{'sales':sales,'total':total,'change':change,'net':net})


@login_required
def doll(request):
    dolls=Doll.objects.all()
    return render(request,'dolls/doll.html',{'dolls':dolls})


@login_required
def sitterpaymentlist(request):
    sitterpayment=Sitterpayment.objects.all()
    return render(request,'baby_payments/sitterpaymentlist.html',{'sitterpayment':sitterpayment})


def delete_baby(request, baby_id):
    baby = get_object_or_404(RegisterBaby, id=baby_id)
    if request.method == 'POST':
        baby.delete()
        return redirect('all_babies')
    return render(request, 'babies/delete.html', {'baby': baby})

# def payment_baby(request):
#     if request.method == 'POST':
#         form = AddPayment(request.POST)
#         if form.is_valid():
#             payment = form.save(commit=False)
#             payment.total_amount_due = calculate_total_amount_due(payment.payment_rate, payment.starting_date, payment.ending_date)
#             payment.save()
#             messages.success(request, 'Payment added successfully')
#             return redirect('/payment_baby')
#     else:
#         form = AddPayment()
#     return render(request, 'payment_baby.html', {'form': form})

# def calculate_total_amount_due(payment_rate, starting_date, ending_date):
#     if payment_rate == 'Full day':
#         return 15000
#     elif payment_rate == 'Half day':
#         return 10000
#     elif payment_rate == 'Monthly':
        
#         weekdays = 0
#         while starting_date <= ending_date:
#             if starting_date.weekday() < 5:  
#                 weekdays += 1
#             starting_date += datetime.timedelta(days=1)
#         return 10000 * weekdays  


#         def _str_(self):
#             return str(self.baby_name)


def payment(request):
    if request.method == 'POST':
        form = Babypayment_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Payment registered successfully')
            return redirect('/payment')
    else:
        form = Babypayment_form()
    return render(request,'baby_payments/payment.html',{'form':form})

def sitterpayment(request):
    if request.method == 'POST':
        form = Sitterpayment_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sitterpaymentlist')
    else:
        form = Sitterpayment_form()
    return render(request,'baby_payments/sitterpayment.html',{'form':form})