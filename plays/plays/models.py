from django.db import models

class Actor(models.Model): 
    name = models.CharField(max_length=255)
    
    def __str__(self): 
        return f'Actor Name: {self.name}'

class Role(models.Model): 
    name_of_role = models.CharField(max_length=255)
    actor = models.ManyToManyField(Actor)
    
    def __str__(self): 
        return f'Role: {self.name_of_role}'

class Play(models.Model): 
    name_of_play = models.CharField(max_length=255) 
    role = models.ManyToManyField(Role)

    def __str__(self): 
        return f'Play Name: {self.name_of_play}'

class Director(models.Model): 
    name = models.CharField(max_length=255)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)

    def __str__(self): 
        return f'Name: {self.name}'

