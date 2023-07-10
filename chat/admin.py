from django.contrib import admin
from .models import Message



class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'author', 'receiver')
    list_display = ('text', 'created_at', 'author', 'receiver') 
    search_fields = ('text', 'author__username', 'receiver__username')
    
    
    
# Register your models here.
admin.site.register(Message, MessageAdmin)