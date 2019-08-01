from django.db import models 


class Worker(models.Model): 
    name = models.CharField(max_length=255) 
    wage = models.DecimalField(max_digits=4, decimal_places=2)
   
    def __str__(self): 
        return f'{self.name} '

class Shift(models.Model): 
    day = models.DateField(auto_now_add=False, blank=True)
    time = models.TimeField(auto_now_add=False)

    def __str__(self): 
        return f'{self.day} '

    
class Shifts(models.Model): 
    all_shifts = models.ForeignKey(Shift, on_delete=models.CASCADE) 
    scheduale = models.ManyToManyField('Worker')

    def __str__(self): 
        return f'Scheduale: {self.all_shifts} '

