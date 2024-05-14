# from django.utils import formats

# formatted_date = formats.date_format(receipt.date_sale, format="DATE_FORMAT")
import django_filters
from .models import *

class SitterFilter(django_filters.FilterSet):
    class Meta:
        model = BabySitter
        fields = ['name']



class Sitter_arrivalFilter(django_filters.FilterSet):
    class Meta:
        model = BabySitterattendance
        fields = ['name'] 

class Baby_Filter (django_filters.FilterSet):
    class Meta:
        model=RegisterBaby
        fields=['Assigned_to'] 


class payment_Filter(django_filters.FilterSet):
    class Meta:
        model = BabyPayment
        fields = ['name']     



class Departure_Filter(django_filters.FilterSet):
    class Meta:
        model = Departure
        fields = ['baby_name']   

class ProcurementFilter(django_filters.FilterSet):
    class Meta:
        model = Inventory
        fields = ['item_name']   

class SitterpaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Sitterpayment
        fields = ['sitter_name'] 

class DollFilter(django_filters.FilterSet):

    class Meta:
        model = Doll
        fields = ['name_of_the_doll']