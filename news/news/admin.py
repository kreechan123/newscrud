from django.contrib import admin

from .models import Category, Newsinfo, Newsimage

admin.site.register(Category)
admin.site.register(Newsinfo)
admin.site.register(Newsimage)
