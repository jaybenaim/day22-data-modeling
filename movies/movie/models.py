from django.db import models 

class Viewer(models.Model): 
    name = models.CharField(max_length=255)
    films = models.ManyToManyField('Film')

    def __str__(self): 
        return f'{self.name} '
        
class Film(models.Model): 
    name_of_film = models.CharField(max_length=255)
    # viewers = models.ForeignKey(Viewer, on_delete=models.CASCADE)

    Viewer = models.ManyToManyField('Viewer')
    def __str__(self): 
        return f'{self.name_of_film}'


class Movies_Viewed(models.Model): 
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.viewer} {self.film}'

