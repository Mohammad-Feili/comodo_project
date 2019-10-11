from django.contrib import admin
from .models import Questions


class QuesAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'subject')
    list_display_links = ('sender_name',)
    list_filter = ('subject', 'sender_name')
    list_editable = ('subject',)
    search_fields = ('sender_id', 'sender_name', 'subject')
    list_per_page = 15


admin.site.register(Questions, QuesAdmin)
