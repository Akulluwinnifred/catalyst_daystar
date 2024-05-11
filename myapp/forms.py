from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.forms import CharField, PasswordInput,TextInput,EmailField, PasswordInput


#baby registration form here
class Babyreg_form(forms.ModelForm):
    class Meta:
        model = RegisterBaby
        fields = '__all__'
        widgets = {
            'Time_In': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
        

#sitter registration form here
class Sitterreg_form(forms.ModelForm):
    class Meta:
        model = BabySitter
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].disabled = True


#sitter attendance form here
class Sittersattendance_form(forms.ModelForm):
    class Meta:
        model = BabySitterattendance
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attendance_status'].disabled = True


#baby departure form here
class Departure_form(forms.ModelForm):
    class Meta:
        model = Departure
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
        

#baby payment form here
class Babypayment_form(forms.ModelForm):
    class Meta:
        model = BabyPayment
        fields = '__all__'


#sitter payment form here
class Sitterpayment_form(forms.ModelForm):
    class Meta:
        model = Sitterpayment
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].disabled = True
        
      
 #password change form here
class PasswordChangeCustomForm(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect': "The old password is incorrect. Please try again"}
    
    old_password = CharField(
        required=True,
        label='Old password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'The password cannot be empty'}
    )

    new_password1 = CharField(
        required=True,
        label='New password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'The password cannot be empty'}
    )

    new_password2 = CharField(
        required=True,
        label='Confirm new password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'The password cannot be empty'}
    )



#doll form here
class  DollForm(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'


#adding doll to stock form
class Addform(ModelForm):
    class Meta:
        model = Doll
        fields = ['received_quantity']



#sales record form here
class SalesrecordForm(ModelForm):
    class Meta:
        model = Salesrecord
        fields = [ 'baby_name', 'quantity_sold', 'amount_received']


#inventory form here
class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['quantity_bought']


#form for issuing out items here   
class Issuingform(ModelForm):
    class Meta:
        model = Issuing
        fields = '__all__'


#form for adding inventory to stock here
class Addingstock(ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name' ,'date_purchased' ,'quantity_bought','amount_in_Ugx']


