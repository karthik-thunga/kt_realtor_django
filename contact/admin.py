from django.contrib import admin
from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','user_id','listings','email','contact_date')
    list_display_links=('id','name')

admin.site.register(Contacts,ContactAdmin)
