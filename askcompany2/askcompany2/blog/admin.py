from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title']