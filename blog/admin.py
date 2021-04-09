from django.contrib import admin
from .models import Post, Category, Comment

# Register models to admin site
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
