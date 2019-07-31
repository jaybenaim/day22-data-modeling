from django.db import models 

class Person(models.Model): 
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    
class Residence(models.Model): 
     address = models.CharField(max_length=255)
     year_built = models.IntegerField() 
     person = models.ForeignKey(Person, on_delete=models.CASCADE) 


class City(models.Model): 
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField() 
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
   
class Province(models.Model): 
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField() 
    city = models.ForeignKey(City, on_delete=models.CASCADE) 

class Country(models.Model): 
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField() 
    national_anthem = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)


