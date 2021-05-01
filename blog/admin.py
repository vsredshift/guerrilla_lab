from django.contrib import admin
from .models import Post, Category, Comment
from .forms import PostForm, FeaturedPost
from mptt.admin import MPTTModelAdmin


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug', 'author')
    readonly_fields = ('slug', )
    # prepopulated_fields = {'slug': ('title',), }
    form = FeaturedPost


# Register models to admin site
# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment, MPTTModelAdmin)
