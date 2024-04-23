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
    name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    Date_Of_Birth = models.DateTimeField(null=True, blank=True)
    NIN = models.IntegerField(null=True, blank=True)
    Religion = models.CharField(max_length=30, null=True, blank=True)
    Level_Of_Education = models.CharField(max_length=200, null=True, blank=True)
    Contact = models.IntegerField(null=True, blank=True)
    Sitter_Number = models.CharField(max_length=200,null=True, blank=True)
    Next_Of_Kin = models.CharField(max_length=200, null=True, blank=True)
    Recommenders_Name = models.CharField(max_length=200, null=True, blank=True)
    Recommenders_Contact = models.IntegerField(null=True, blank=True)

class RegisterBaby(models.Model):
    c_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True,blank=True)
    c_fee = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    Date_Of_Birth = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    Baby_Number = models.CharField(max_length=200,null=True, blank=True, default=0)
    Parents_Name = models.CharField(max_length=200,null=True, blank=True)
    Brought_by = models.CharField(max_length=200, null=True, blank=True)
    Picked_up_by = models.CharField(max_length=200, null=True, blank=True)
    TimeIn = models.DateTimeField(null=True, blank=True)
    TimeOut = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.name


# class AddBaby(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#     gender = models.CharField(max_length=10, null=True, blank=True)
#     age = models.IntegerField(null=True, blank=True, default=0)
#     DateOfBirth = models.IntegerField(null=True, blank=True, default=0)
#     location = models.CharField(max_length=100, null=True, blank=True)
#     BabyNumber = models.CharField(max_length=200,null=True, blank=True, default=0)
#     FeeInUgx = models.IntegerField(null=True, blank=True, default=0)
#     ParentsOrGuardiansName = models.CharField(max_length=200, null=True, blank=True)
#     ParentsOrGuardiansConatct = models.CharField(max_length=200,null=True, blank=True)
#     PeriodOfStay = models.CharField(max_length=200,null=True, blank=True)
#     DateOfRegistartion= models.DateTimeField(null=True, blank=True, default=0)
#     MoreInfromationAboutTheBaby = models.TextField(max_length=500, null=True, blank=True)

class InventoryTracker(models.Model):
    product = models.CharField(max_length=200, null=True, blank=True)
    UnitPrice = models.IntegerField(null=True, blank=True, default=0)
    QuantityPrice = models.IntegerField(null=True, blank=True, default=0)
    TotalPrice = models.IntegerField(null=True, blank=True, default=0)
    TotalAmount = models.IntegerField(null=True, blank=True, default=0)

# class Sitterreg(models.Model):
#     GENDER_CHOICES = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#     )

#     first_name = models.CharField(max_length=30, null=False, blank=False)
#     last_name = models.CharField(max_length=30, null=False, blank=False)
#     Date_of_birth = models.DateTimeField(null=True, blank=True,)
#     contact = models.IntegerField()
#     location = models.CharField(max_length=30, null=False, blank=False)
#     Gender = models.CharField(max_length=10, null=False, blank=False, choices=GENDER_CHOICES)
#     Level_of_education = models.CharField(max_length=30, null=False, blank=False)
#     Next_of_kin = models.CharField(max_length=30, null=False, blank=False)
#     Sitter_number = models.CharField(max_length=30, null=False, blank=False)
#     NIN = models.CharField(max_length=30, null=False, blank=False)
#     Recommenders_name = models.CharField(max_length=30, null=False, blank=False)
#     Religion = models.CharField(max_length=30, null=True, blank=True)

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
   


