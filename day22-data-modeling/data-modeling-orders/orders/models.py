from django.db import models 


class Order(models.Model): 
    order_number = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True) 

class Customer(models.Model): 
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mailing_address = models.TextField() 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="customers")

