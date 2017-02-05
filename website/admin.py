from django.contrib import admin
from .models import Comment
from .models import Book
from .models import Page
from .models import Category

# Register your models here.
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Page)
admin.site.register(Category)
