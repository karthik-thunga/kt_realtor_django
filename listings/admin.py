from django.contrib import admin

from .models import Listings


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'realtor', 'price', 'is_published')
    list_display_links = ('title', 'id')
    list_filter = ('realtor',)
    list_editable = ('is_published', )
    search_fields = ('id', 'title', 'realtor', 'price')
    list_per_page = 25


admin.site.register(Listings, ListingAdmin)
