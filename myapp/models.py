from django.db import models
# from django.contrib.auth .models import User
# from django.shortcuts import render
from django.utils import timezone

# Create your models here.

class Categorystay(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)
    def __str__(self):
        return self.name
    
class Payment(models.Model):
    c_payment = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True,blank=True)
    payment_number = models.IntegerField(null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True,default=0)
    currency = models.CharField(max_length=5,default='Ugx',null=True,blank=True)

    def __int__(self):
        return self.payment_number

class BabySitter(models.Model):
    GENDER_CHOICES = (
         ('male', 'Male'),
        ('female', 'Female'),
     )
    name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True,choices=GENDER_CHOICES)
    location = models.CharField(max_length=100, null=True, blank=True)
    Date_Of_Birth = models.DateTimeField(null=True, blank=True)
    NIN = models.CharField(max_length=14,null=True, blank=True)
    Religion = models.CharField(max_length=30, null=True, blank=True)
    Level_Of_Education = models.CharField(max_length=200, null=True, blank=True)
    Contact = models.IntegerField(null=True, blank=True)
    Sitter_Number = models.CharField(max_length=200,null=True, blank=True)
    Next_Of_Kin = models.CharField(max_length=200, null=True, blank=True)
    Recommenders_Name = models.CharField(max_length=200, null=True, blank=True)
    Recommenders_Contact = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class RegisterBaby(models.Model):
    GENDER_CHOICES = (
         ('male', 'Male'),
        ('female', 'Female'),
     )
    Period_of_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True,blank=True)
    Fee = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True,choices=GENDER_CHOICES)
    age = models.IntegerField(null=True, blank=True, default=0)
    Date_Of_Birth = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    Baby_Number = models.CharField(max_length=200,null=True, blank=True, default=0)
    Parents_Name = models.CharField(max_length=200,null=True, blank=True)
    Brought_by = models.CharField(max_length=200, null=True, blank=True)
    Time_In = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

class Departure(models.Model):
    baby_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    picked_up_by = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name




class InventoryTracker(models.Model):
    product = models.CharField(max_length=200, null=True, blank=True)
    UnitPrice = models.IntegerField(null=True, blank=True, default=0)
    QuantityPrice = models.IntegerField(null=True, blank=True, default=0)
    TotalPrice = models.IntegerField(null=True, blank=True, default=0)
    TotalAmount = models.IntegerField(null=True, blank=True, default=0)



#     def __str__(self):
#         return self.first_name

    

# class Babyreg(models.Model):
#     GENDER_CHOICES = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#     )
#     first_name = models.CharField(max_length=30, null='False',blank = 'False')
#     last_name = models.CharField(max_length=30, null='False',blank = 'False')
#     Age = models.IntegerField()
#     location = models.CharField(max_length=30, null='False',blank = 'False')
#     Gender =  models.CharField(max_length=10,null="False",blank = "False",choices=GENDER_CHOICES)
#     Parents_name = models.CharField(max_length=30, null='False',blank = 'False')
#     Baby_number = models.CharField(max_length=30, null='False',blank = 'False')
#     def __str__(self):
#         return self.first_name 
    

# class Signup(models.Model):
#     Username = models.CharField(max_length=30, null='False',blank = 'False')
#     Email = models.EmailField(max_length=30, null='False',blank = 'False')
#     Password = models.CharField(max_length=12, null='False',blank = 'False')
#     Confirm_password = models.CharField(max_length=12, null='False',blank = 'False')


# class Forgotpassword(models.Model):
#     Email = models.EmailField(max_length=30, null='False',blank = 'False')


# class Arrival(models.Model):
#    Baby_Name = models.CharField(max_length=30, null='False',blank = 'False')
#    Brought_by = models.CharField(max_length=30, null='False',blank = 'False')
#    Time_in = models.DateTimeField(auto_now_add=True)
#    Date = models.DateTimeField(auto_now_add=True)
#    comment = models.CharField(max_length=30, null='False',blank = 'False')

# class Departure(models.Model):
#    Baby_Name = models.CharField(max_length=30, null='False',blank = 'False')
#    Picked_by = models.CharField(max_length=30, null='False',blank = 'False')
#    Time_out = models.DateTimeField(auto_now_add=True)
#    comment = models.CharField(max_length=30, null='False',blank = 'False')
   


