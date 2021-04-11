from django.contrib import admin
from .models import Post, Category, Comment


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


# Register models to admin site
# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
