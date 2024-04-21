from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.forms import CharField, PasswordInput,TextInput,EmailField, PasswordInput
# class Sitterreg_form(forms.ModelForm):
#     class Meta:
#         model = Sitterreg
#         fields=['first_name','last_name','Date_of_birth','contact','location','Gender','Level_of_education','Next_of_kin','Sitter_number','NIN','Recommenders_name','Religion']


class Babyreg_form(forms.ModelForm):
    class Meta:
        model = RegisterBaby
        fields = '__all__'
        # fields = [
        #     'c_fee','name','c_stay','gender','age','DateOfBirth','location','BabyNumber','Parents_Name','NameOfThePersonThatHasBroughtTheBaby','NameOfThePersonThatHasTakenTheBaby','TimeIn','TimeOut',
        #     'Comment'
        # ]
 








  




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


# class Signup_form(forms.ModelForm):
#     class Meta:
#         model = Signup
#         fields=['Username','Email','Password','Confirm_password']


# class Arrival_form(forms.ModelForm):
#     class Meta:
#         model = Arrival
#         fields=['Baby_Name','Brought_by','comment']

# class Departure_form(forms.ModelForm):
#     class Meta:
#         model = Departure
#         fields=['Baby_Name','Picked_by','comment']

# class Forgotpassword_form(forms.ModelForm):
#     class Meta:
#         model = Forgotpassword
#         fields=['Email']


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        # Add custom email validation if needed
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be from gmail.com domain.")
        return email