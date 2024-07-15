from django.contrib import admin
from .models import Contact,Blog,Portfolio,Team,PortfolioCategory
from django.utils.html import format_html
# Register your models here.

admin.site.register((Contact,Portfolio,Team,PortfolioCategory)) 

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','img')
    readonly_fields = ['slug']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))