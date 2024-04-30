from django.db import models
from django.utils import timezone


class Categorystay(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.name
    
class Paymenttype(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.name
    
    #baby payments

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
    Date_Of_Birth = models.DateField(default=timezone.now)
    NIN = models.CharField(max_length=14)
    Religion = models.CharField(max_length=30, null=True, blank=True,verbose_name="Religion(optional)")
    Level_Of_Education = models.CharField(max_length=200,choices=(
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('Degree', 'Degree'),
        ('Others', 'Others'),
    ))
    Contact = models.CharField(max_length=15)
    Sitter_Number = models.CharField(max_length=200,unique=True,blank=True, null=True)
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
    # Fee = models.ForeignKey(Payment, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    Period_of_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    Baby_Number = models.CharField(max_length=200,default=0)
    Parents_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Arrivalbaby(models.Model):
       baby_name = models.ForeignKey(RegisterBaby, on_delete=models.CASCADE,null=True,blank=True)
       Baby_Number = models.CharField(max_length=200,default=0)
       Period_of_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE)
       Brought_by = models.CharField(max_length=200)
       Time_In = models.DateTimeField()
       created_at = models.TimeField(auto_now_add=True)
       
       def __str__(self):
          return self.Baby_Number
       
class Payment(models.Model):
    baby_name = models.ForeignKey(RegisterBaby, on_delete=models.CASCADE,null=True,blank=True)
    payment_rate = models.ForeignKey(Paymenttype, on_delete=models.CASCADE)
    currency = models.CharField(max_length=5,default='Ugx')
    amount_due = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    remaining_balance = models.IntegerField(default=0)
    payment_status = models.CharField(max_length=200, choices=(
        ('complete', 'complete'),
        ('pending', 'pending'),
    ))
    paid_by = models.CharField(max_length=200,)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return (self.baby_name)




class Departure(models.Model):
    baby_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    picked_up_by = models.CharField(max_length=100)
    comment = models.TextField(blank=True,verbose_name="Comment(optional)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baby_name
    


class BabySitterattendance(models.Model):
     STATUS_CHOICES = (
         ('On_duty', 'On_duty'),
     )
     sitter_Number = models.CharField(max_length=200)
     name = models.ForeignKey(BabySitter, on_delete=models.CASCADE)
     date = models.DateField(default=timezone.now)
     attendance_status = models.CharField(max_length=10,choices=STATUS_CHOICES)

     def __str__(self):
        return self.name


# class InventoryTracker(models.Model):
#     product = models.CharField(max_length=200)
#     Unit_Price = models.IntegerField(default=0)
#     Quantity_Price = models.IntegerField(default=0)
#     Total_Price = models.IntegerField(default=0)
#     Total_Amount = models.IntegerField(default=0)


class Category_doll(models.Model):  
     name = models.CharField(max_length=100,null=True, blank=True)

     def __str__(self):
        return self.name  


class Doll(models.Model):
    c_doll=models.ForeignKey(Category_doll, on_delete=models.CASCADE,null=True, blank=True)
    name_of_the_doll =models.CharField(max_length=200,null=True, blank=True)
    quantity=models.IntegerField(default=0)
    color=models.CharField(max_length=200, null=True,blank=True)
    size=models.CharField(max_length=200,null=True,blank=True)
    issued_quantity=models.IntegerField(default=0,blank=True,null=True) 
    received_quantity=models.IntegerField(default=0,null=True,blank=True)
    Unit_price=models.IntegerField(default=0,null=True, blank=True)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name_of_the_doll
    
class Salesrecord(models.Model):    
    doll=models.ForeignKey(Doll,  on_delete=models.CASCADE,null=False, blank=False)
    baby_name=models.CharField(max_length=200)
    paid_by=models.CharField(max_length=200,null=True,blank=True)
    quantity_sold=models.IntegerField(default=0)
    amount_received=models.IntegerField(default=0)
    sale_date=models.DateField(default=timezone.now)
    unit_price=models.IntegerField(default=0)
     
    
    def get_total(self):
        total= self.quantity_sold * self.unit_price
        return int( total)
    
#here we are getting change.(money to be given to theparent)    
    def get_change(self):
        change= self.get_total() - self.amount_received
        return int(change)#sales is linked to products

