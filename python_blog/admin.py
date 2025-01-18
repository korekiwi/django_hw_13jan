from django.contrib import admin
from python_blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ["title", "published_date", "updated_date", "category"]
    readonly_fields = ["slug"]
