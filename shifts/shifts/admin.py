from django.contrib import admin 
from shifts.models import * 

admin.site.register(Worker)
admin.site.register(Shift)
admin.site.register(Shifts)