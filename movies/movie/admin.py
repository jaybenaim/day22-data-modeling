from django.contrib import admin 
from movie.models import * 

admin.site.register(Viewer)
admin.site.register(Film)
admin.site.register(Movies_Viewed) 