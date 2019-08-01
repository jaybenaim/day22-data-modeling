from django.db import models



class Reader(models.Model): 
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Chapter(models.Model): 
    title = models.CharField(max_length=255)
    books = models.ManyToManyField('Book', blank=True)

    def __str__(self):
        return f'{self.title}'


class Author(models.Model): 
    name = models.CharField(max_length=255) 
    books = models.ManyToManyField('Book', blank=True) 

    def __str__(self):
        return f'{self.name}'


class Book(models.Model): 
    title = models.CharField(max_length=255)
    year = models.DateField(auto_now_add=False, blank=True)
    chapters = models.ManyToManyField('Chapter', blank=True)
    readers = models.ManyToManyField('Reader', blank=True)
    authors = models.ManyToManyField('Author', blank=True)

    
    # def get_year(self): 
    #     return self.get_year.year



