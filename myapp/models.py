from django.db import models
from django.utils import timezone
import re
from django.core.exceptions import ValidationError



# Create your models here.

#models for category stay
class Categorystay(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.name
    

#letter validation
def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")

#number validation function
def validate_numbers(value):
    if not re.match("^[0-9]*$", value):
        raise ValidationError("Only numbers are allowed.")

#contact length validation function
def validate_contact_length(value):
    if len(value) != 10:
        raise ValidationError("Contact field must contain exactly 10 digits.")

#NIN length validation function
def validate_NIN_length(value):
    if len(value) != 14:
        raise ValidationError("NIN field must contain exactly 14 digits.")


#babysitter model here
class BabySitter(models.Model):

    GENDER_CHOICES = (
         ('male', 'Male'),
        ('female', 'Female'),
     )
    
    name = models.CharField(max_length=200,validators=[validate_letters])
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    location = models.CharField(max_length=10, default='kabalagala')
    Date_Of_Birth = models.DateField(default=timezone.now)
    NIN = models.CharField(max_length=14,validators=[validate_NIN_length])
    Religion = models.CharField(max_length=30, null=True, blank=True,verbose_name="Religion(optional)")
    Level_Of_Education = models.CharField(max_length=200,choices=(
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('Degree', 'Degree'),
        ('Others', 'Others'),
    ))
    Contact = models.CharField(max_length=10,validators=[validate_contact_length])
    Sitter_Number = models.CharField(max_length=200,unique=True,blank=False, null=True)
    Next_Of_Kin = models.CharField(max_length=200,validators=[validate_letters])
    Recommenders_Name = models.CharField(max_length=200,validators=[validate_letters])
    Recommenders_Contact = models.CharField(max_length=10,validators=[validate_contact_length])
    
    
    def __str__(self):
        return self.name

#siter attendance model here
class BabySitterattendance(models.Model):
    name = models.ForeignKey(BabySitter, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    attendance_status = models.CharField(max_length=10,default= 'Onduty')

    def __str__(self):
        return str(self.name)


#baby registration model here
class RegisterBaby(models.Model):

    GENDER_CHOICES = (
         ('male', 'Male'),
        ('female', 'Female'),
     )
    name = models.CharField(max_length=200,validators=[validate_letters])
    Baby_Number = models.CharField(max_length=200,unique=True,blank=False, null=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    Period_of_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    Parents_Name = models.CharField(max_length=200,validators=[validate_letters])
    Period_of_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE)
    Brought_by = models.CharField(max_length=200,validators=[validate_letters])
    Fee_in_UGX = models.IntegerField()
    Assigned_to = models.ForeignKey(BabySitterattendance, on_delete=models.CASCADE)
    Time_In = models.DateTimeField()

    def __str__(self):
        return self.name
    

#baby departure model here
class Departure(models.Model):
    baby_name = models.ForeignKey(RegisterBaby, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    picked_up_by = models.CharField(max_length=100,validators=[validate_letters])
    comment = models.TextField(blank=True,verbose_name="Comment(optional)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baby_name
    

#dolls category model here
class Category_doll(models.Model):  
     name = models.CharField(max_length=100,null=True, blank=True)

     def __str__(self):
        return self.name  

#dolls model here
class Doll(models.Model):
    c_doll=models.ForeignKey(Category_doll, on_delete=models.CASCADE,null=True, blank=True)
    name_of_the_doll =models.CharField(max_length=200,null=True, blank=True)
    quantity=models.IntegerField(default=0)
    color=models.CharField(max_length=200, null=True,blank=True,validators=[validate_letters])
    size=models.CharField(max_length=200,null=True,blank=True)
    issued_quantity=models.IntegerField(default=0,blank=True,null=True) 
    received_quantity=models.IntegerField(default=0,null=True,blank=True)
    Unit_price=models.IntegerField(default=0,null=True, blank=True)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name_of_the_doll


#sales record for doll model here
class Salesrecord(models.Model):    
    doll=models.ForeignKey(Doll,  on_delete=models.CASCADE,null=False, blank=False)
    baby_name=models.ForeignKey(RegisterBaby, on_delete=models.CASCADE)
    paid_by=models.CharField(max_length=200,null=True,blank=True,validators=[validate_letters])
    quantity_sold=models.IntegerField(default=0)
    amount_received=models.IntegerField(default=0)
    sale_date=models.DateField(default=timezone.now)
    unit_price=models.IntegerField(default=0)
     
    
    def get_total(self):
        total= self.quantity_sold * self.unit_price
        return int( total)
    
#here i are getting change.(money to be given to the parent)    
    def get_change(self):
        change= self.get_total() - self.amount_received
        return int(change)#sales is linked to products


#baby payment model here
class BabyPayment(models.Model):
    name = models.CharField(max_length=200,validators=[validate_letters])
    payment_date = models.DateField()
    full_day = models.BooleanField(default=False,blank=True)
    half_day = models.BooleanField(default=False,blank=True)
    monthly = models.BooleanField(default=False,blank=True)
    monthly = models.BooleanField(default=False,blank=True)
    total_amount_due = models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2,default=False,blank=True)
    def __str__(self):
        return self.name
    

#sitter payment model here
class Sitterpayment(models.Model):
    sitter_name=models.ForeignKey(BabySitterattendance, on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    baby_count=models.IntegerField(default=0)
    amount=models.IntegerField(default=3000)
    
    def _str_(self):
        return f"Sitter Payment - {self.sitter_name}"

    def total_amount(self):
        total= self.amount * self.baby_count
        return int(total)

 #model for category items here   
class Items(models.Model):
        name = models.CharField(max_length=50, null=True,blank=True)

        def __str__(self):
            return self.name


#inventory form model here
class Inventory(models.Model):
    item_name = models.ForeignKey(Items, on_delete=models.CASCADE,null=True,blank=True)
    date_purchased = models.DateField(default=timezone.now)
    quantity_bought = models.IntegerField(default=0)
    amount_in_Ugx = models.IntegerField()
    quantity_issued_out = models.IntegerField(default=0)
    quantity_in_stock = models.IntegerField(default=0)
    stock_at_hand = models.IntegerField(default=0)

    def __str__(self):
        return str(self.item_name)

    #calculating the stock at hand (total stock available)
    def stock_at_hand(self):
        totalquantity = self.quantity_in_stock + self.quantity_bought
        return totalquantity
    

#form for issuing out inventory
class Issuing(models.Model):
    quantity_issued_out = models.IntegerField(default=0)





