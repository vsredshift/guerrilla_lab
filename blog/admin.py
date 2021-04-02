from django.contrib import admin
from .models import Post, Category

# Register models to admin site
admin.site.register(Post)
admin.site.register(Category)
