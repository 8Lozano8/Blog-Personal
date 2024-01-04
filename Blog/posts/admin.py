from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class PostsAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(Post, PostsAdmin)
admin.site.register(Comment)