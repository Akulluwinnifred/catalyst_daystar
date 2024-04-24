from django.db import models
from django.utils import timezone


class Categorystay(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.name
    
    
class Payment(models.Model):
    period_of_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True,blank=True)
    payment_number = models.IntegerField()
    amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=5,default='Ugx')
    paid_by = models.CharField(max_length=200,)

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
    
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    location = models.ForeignKey(FixedLocation, on_delete=models.CASCADE)
    Date_Of_Birth = models.DateTimeField()
    NIN = models.CharField(max_length=14)
    Religion = models.CharField(max_length=30, null=True, blank=True)
    Level_Of_Education = models.CharField(max_length=200)
    Contact = models.CharField(max_length=15)
    Sitter_Number = models.CharField(max_length=200)
    Next_Of_Kin = models.CharField(max_length=200)
    Recommenders_Name = models.CharField(max_length=200)
    Recommenders_Contact = models.IntegerField()
    
    def __str__(self):
        return self.name


class RegisterBaby(models.Model):

    GENDER_CHOICES = (
         ('male', 'Male'),
        ('female', 'Female'),
     )
    
    Period_of_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE)
    # Fee = models.ForeignKey(Payment, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    Date_Of_Birth = models.DateTimeField()
    location = models.CharField(max_length=100)
    Baby_Number = models.CharField(max_length=200,default=0)
    Parents_Name = models.CharField(max_length=200)
    Brought_by = models.CharField(max_length=200)
    Time_In = models.DateTimeField()
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
    


class BabySitterattendance(models.Model):
     STATUS_CHOICES = (
         ('On_duty', 'On_duty'),
        ('Off_duty', 'Off_duty'),
     )
     name = models.CharField(max_length=100)
     date = models.DateTimeField()
     attendance_status = models.CharField(max_length=10,choices=STATUS_CHOICES)






class InventoryTracker(models.Model):
    product = models.CharField(max_length=200)
    Unit_Price = models.IntegerField(default=0)
    Quantity_Price = models.IntegerField(default=0)
    Total_Price = models.IntegerField(default=0)
    Total_Amount = models.IntegerField(default=0)



