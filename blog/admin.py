from django.contrib import admin
from .models import Post, Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'category')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_editable = ('category',)
    search_fields = ('title', 'name', 'category')
    list_per_page = 25


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_id', 'post_id')
    list_display_links = ('name', 'parent_id')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Comments, CommentAdmin)
