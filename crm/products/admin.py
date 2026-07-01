from django.contrib import admin
from .models import Author, Book,Product,Tag

# Register your models here.
admin.site.register([Author, Book, Product, Tag])

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     model = Author
    