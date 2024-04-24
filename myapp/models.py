from django.db import models
from django.utils import timezone


class Categorystay(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.name
    
    
class Payment(models.Model):
    period_of_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True,blank=True)
    payment_number = models.IntegerField(null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True,default=0)
    currency = models.CharField(max_length=5,default='Ugx',null=True,blank=True)
    paid_by = models.CharField(max_length=200, null=True, blank=True)

    def __int__(self):
        return self.payment_number


class FixedLocation(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class BabySitter(models.Model):

    GENDER_CHOICES = (
         ('male', 'Male'),
        ('female', 'Female'),
     )
    
    name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True,choices=GENDER_CHOICES)
    location = models.ForeignKey(FixedLocation, on_delete=models.CASCADE)
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



