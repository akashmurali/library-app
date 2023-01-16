from django.contrib import admin
from .models import *

class StaffAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'user', 'name', 'email', 'phone','email',)
    ordering = ('name',)
    search_fields = ('name', )
    
admin.site.register(Staff, StaffAdmin)