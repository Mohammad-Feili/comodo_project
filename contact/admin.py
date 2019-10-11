from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    list_editable = ('email', 'phone')
    list_display_link = ('name', 'email')
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)
