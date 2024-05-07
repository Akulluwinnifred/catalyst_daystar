from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.forms import CharField, PasswordInput,TextInput,EmailField, PasswordInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

# Your existing code here...



class Babyreg_form(forms.ModelForm):
    class Meta:
        model = RegisterBaby
        fields = '__all__'
        widgets = {
            'Time_In': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
        

class Sitterreg_form(forms.ModelForm):
    class Meta:
        model = BabySitter
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].disabled = True


class Sittersattendance_form(forms.ModelForm):
    class Meta:
        model = BabySitterattendance
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attendance_status'].disabled = True


# class Assignbabies_form(forms.ModelForm):
#     class Meta:
#         model = Assignbabies
#         fields = '__all__'
    

class Payment_form(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['currency'].disabled = True

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'baby_name',
            'period_of_stay',
            'payment_rate',
            'currency',
            'amount_due',
            'amount_paid',
            'remaining_balance',
            'payment_status',
            'paid_by',
            'date',
        )
        self.fields['period_of_stay'].widget.attrs['onchange'] = 'calculateAmountDue()'
        self.fields['payment_rate'].widget.attrs['onchange'] = 'calculateAmountDue()'

    def clean(self):
        cleaned_data = super().clean()
        period_of_stay = cleaned_data.get('period_of_stay')
        payment_rate = cleaned_data.get('payment_rate')
        print("Period of Stay:", period_of_stay)
        print("Payment Rate:", payment_rate)

        if period_of_stay and payment_rate:
            if period_of_stay.name == "Half day":
                if payment_rate.name == "Monthly":
                    cleaned_data['amount_due'] = 10000 * 30
                else:
                    cleaned_data['amount_due'] = 10000
            else:  # Assuming period_of_stay is "Full day"
                if payment_rate.name == "Monthly":
                    cleaned_data['amount_due'] = 15000 * 30
                else:
                    cleaned_data['amount_due'] = 15000

        return cleaned_data

class Departure_form(forms.ModelForm):
    class Meta:
        model = Departure
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
        
class Babypayment_form(forms.ModelForm):
    class Meta:
        model = BabyPayment
        fields = '__all__'


class Sitterpayment_form(forms.ModelForm):
    class Meta:
        model = Sitterpayment
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].disabled = True
        
      
 
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
        fields = ['received_quantity']

class SalesrecordForm(ModelForm):
    class Meta:
        model = Salesrecord
        fields = [ 'baby_name', 'quantity_sold', 'amount_received']


class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['quantity_bought']
    
class Issuingform(ModelForm):
    class Meta:
        model = Issuing
        fields = '__all__'

class Addingstock(ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name' ,'date_purchased' ,'quantity_bought','amount_in_Ugx']