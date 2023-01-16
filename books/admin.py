from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('auto_id',  'name', 'author')
    ordering = ('name',)
    search_fields = ('name', 'author')
    
admin.site.register(Book, BookAdmin)

class BookRequestAdmin(admin.ModelAdmin):
    list_display = ('auto_id',  'customer', 'book','is_accepted','is_completed')
    ordering = ('date_added',)
    search_fields = ('customer','book', 'is_accepted','is_completed',)
    
admin.site.register(BookRequest, BookRequestAdmin)