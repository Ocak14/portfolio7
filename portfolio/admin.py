from django.contrib import admin
from .models import Contact,Blog,Portfolio,Category,Team,PortfolioCategory
from django.utils.html import format_html
from django.db import models
# Register your models here.

admin.site.register((Contact,Portfolio,Category,PortfolioCategory)) 

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','img')
    readonly_fields = ['slug']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))
  

@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ('img','full_name','job')
    readonly_fields = ['id']
    def img(self, obj):
         return format_html(
    '<img width="100" height="100" src="{}" style="border-radius: 50%;" />',
    obj.image.url
)