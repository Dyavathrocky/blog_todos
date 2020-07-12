from django.contrib import admin

from .models import Post

# Register your models here.



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author' , 'title' , 'body' , 'created_at' , 'updated_at']

admin.site.register(Post , AuthorAdmin)