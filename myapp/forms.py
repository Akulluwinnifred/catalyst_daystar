from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.forms import CharField, PasswordInput,TextInput,EmailField, PasswordInput


class Babyreg_form(forms.ModelForm):
    class Meta:
        model = RegisterBaby
        fields = '__all__'
        widgets = {
            'Time_In': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
        

class Babyarrivalform(forms.ModelForm):
    class Meta:
        model = Arrivalbaby
        fields = '__all__'
        widgets = {
            'Time_In': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}


class Sitterreg_form(forms.ModelForm):
    class Meta:
        model = BabySitter
        fields = '__all__'


class Sittersattendance_form(forms.ModelForm):
    class Meta:
        model = BabySitterattendance
        fields = '__all__'

class Payment_form(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
     


class Departure_form(forms.ModelForm):
    class Meta:
        model = Departure
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
      
 
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


class  DollForm(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'

class Addform(ModelForm):
    class Meta:
        model = Doll
        fields = [ 'c_doll', 'received_quantity']

class SalesrecordForm(ModelForm):
    class Meta:
        model = Salesrecord
        fields = [ 'baby_name', 'quantity_sold', 'amount_received']