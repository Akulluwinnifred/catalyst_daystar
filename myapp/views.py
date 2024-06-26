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
from django.db.models import Sum
from .filters import *

#views here

#authentication views
def index(request):
    return render(request,'index.html')


#login view here
def login(request):
    return render(request,'access/login.html')


#logout view here
def logout(request):
    return render(request,'access/logout.html')


#password change view here
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


#base view
@login_required
def base(request):
    return render(request,'base.html')



#babies views

#all babies view here
@login_required
def all_babies(request):
   babies =RegisterBaby.objects.all().order_by('id')
   baby_filter=Baby_Filter(request.GET,queryset = babies)
   babies = baby_filter.qs
   return render(request,'babies/all_babies.html',{'babies':babies,'baby_filter':baby_filter})


#baby registration view here
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
          return render(request,'babies/babyreg.html',{'form':form})
   else:
      form = Babyreg_form()
   return render(request,'babies/babyreg.html',{'form':form})


#baby departure view here 
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


#read baby view here
@login_required
def read(request,id):
    babies_informations =RegisterBaby.objects.get(id=id)
    return render(request,'babies/read.html',{'babies_informations':babies_informations})

#read sitter view here
@login_required
def readsitter(request,id):
    sitters =BabySitter.objects.get(id=id)
    return render(request,'sitters/readsitter.html',{'sitters':sitters})


#baby departure view here
@login_required
def babiesdeparture(request):
    babiesdeparture = Departure.objects.all().order_by('id')
    baby_filter=Departure_Filter(request.GET,queryset = babiesdeparture)
    babiesdeparture = baby_filter.qs
    return render(request,'babies/signedout.html',{'babiesdeparture':babiesdeparture,'baby_filter':baby_filter})


#view for edit baby here
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



#sitters views

#sitter registration view here
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


#sitter attendance view here
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



#registered sitters view here
@login_required
def sitters(request):
    sitters = BabySitter.objects.all().order_by('id')
    sitter_filter=SitterFilter(request.GET,queryset = sitters)
    sitters = sitter_filter.qs
    return render(request,'sitters/all_sitters.html',{'sitters':sitters,'sitter_filter':sitter_filter})


#onduty sitters view here
@login_required
def onduty(request):
    sitters = BabySitterattendance.objects.all().order_by('id')
    sitterarrival=Sitter_arrivalFilter(request.GET,queryset=sitters)
    sitters = sitterarrival.qs
    return render(request,'sitters/onduty.html',{'sitters':sitters,'sitterarrival':sitterarrival})


#inventory views

#views for adding new item to the inventory here
@login_required
def inventory(request,pk):
    new_item=Inventory.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            quantity_bought = form.cleaned_data.get('quantity_bought')
            added_quantity=int(quantity_bought)
            new_item.quantity_in_stock+=added_quantity
            new_item.save()
            return redirect('/allstock')
    else:
        form = InventoryForm()
    return render(request, 'procurement/addstock.html', {'form': form})



#views for issuing out inventory here
@login_required
def issuing(request,pk):
    issued_item = Inventory.objects.get(id=pk)
    form = Issuingform(request.POST)

    if request.method == 'POST':
        form = Issuingform(request.POST)
        if form.is_valid():
            new_issue = form.save(commit = False)
            new_issue.Inventory=issued_item
            new_issue.save()
            issued_quantity = int(request.POST['quantity_issued_out'])
            issued_item.quantity_in_stock -=issued_quantity
            issued_item.save()
            return redirect('/allstock')
    else:
        form = Issuingform()
    return render(request, 'procurement/issuing.html', {'form': form})
    


#all stocks view here
@login_required
def allstock(request):
    stocks = Inventory.objects.all().order_by('id')
    stock_filter=ProcurementFilter(request.GET,queryset=stocks)
    stocks = stock_filter.qs
    return render(request,'procurement/allstock.html',{'stocks':stocks,'stock_filter':stock_filter})



#views for issuing out dolls here
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


#receipt views here
@login_required
def receipt(request):
    sales= Salesrecord.objects.all().order_by('-id') 
    return render(request,'dolls/receipt.html',{'sales':sales})  



#receipt details here
@login_required
def receipt_detail(request, receipt_id):
            receipt = Salesrecord.objects.get(id=receipt_id)
            return render(request,'dolls/receipt_detail.html',{'receipt':receipt})



#dashboard views
@login_required
def home(request):
    # Statistics
    count_babies = RegisterBaby.objects.count()
    count_sitters = BabySitter.objects.count()
    count_departure = Departure.objects.count()
    count_sitterattendance = BabySitterattendance.objects.count()
    context = {
        "count_babies": count_babies,
        "count_sitters": count_sitters,
        "count_departure": count_departure,
        "count_sitterattendance": count_sitterattendance,
    }
    template = loader.get_template("home.html")
    return HttpResponse(template.render(context))



#doll inventory views

#views of adding to stock form here
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


#views of all sales here
@login_required
def all_sales(request):
    sales=Salesrecord.objects.all()
    total=sum([items.amount_received for items in sales])
    change=sum([items.get_change() for items in sales])
    net=total-change
    return render(request,'dolls/all_sales.html',{'sales':sales,'total':total,'change':change,'net':net})



#list of dolls views here
@login_required
def doll(request):
    dolls=Doll.objects.all().order_by('id')
    doll_filter=DollFilter(request.GET,queryset=dolls)
    dolls = doll_filter.qs
    return render(request,'dolls/doll.html',{'dolls':dolls,'doll_filter':doll_filter})


#sitterpayment list views here
@login_required
def sitterpaymentlist(request):
    sitterpayment=Sitterpayment.objects.all().order_by('id')
    sitterpayment_filter=SitterpaymentFilter(request.GET,queryset=sitterpayment)
    sitterpayment = sitterpayment_filter.qs
    return render(request,'baby_payments/sitterpaymentlist.html',{'sitterpayment':sitterpayment,'sitterpayment_filter':sitterpayment_filter})


#baby paymentlist views here
@login_required
def babypaymentlist(request):
    payment=BabyPayment.objects.all().order_by('id')
    payment_filter=payment_Filter(request.GET,queryset=payment)
    payment = payment_filter.qs
    return render(request,'baby_payments/babypaymentlist.html',{'babypayment':payment,'payment_filter':payment_filter})


#baby payment views here
def payment(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        payment_date=request.POST.get('date')
        full_day=request.POST.get('full_day') == 'on'
        half_day=request.POST.get('half_day') ==  'on'
        monthly=request.POST.get('monthly') == 'on'
        total_amount_due=request.POST.get('total_amount')
        amount_paid=request.POST.get('amount_paid')
        remaining_balance=request.POST.get('remaining_balance')
        pay = BabyPayment(name=name,payment_date=payment_date,total_amount_due=total_amount_due,amount_paid=amount_paid
                          ,full_day=full_day,half_day=half_day,monthly=monthly,remaining_balance=remaining_balance)
        pay.save()
        return redirect('/babypaymentlist')
    else:
        return render(request,'baby_payments/payment.html')


#sitter payment views here
def sitterpayment(request):
    if request.method == 'POST':
        form = Sitterpayment_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sitterpaymentlist')
    else:
        form = Sitterpayment_form()
    return render(request,'baby_payments/sitterpayment.html',{'form':form})


#views for adding stock here
def adding(request):
    if request.method == 'POST':
        form = Addingstock(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allstock')
    else:
        form = Addingstock()
    return render(request,'procurement/adding.html',{'form':form})





