from django.contrib import admin
from .models import Contact,Blog,Portfolio,Team,PortfolioCategory

# Register your models here.

admin.site.register((Contact,Blog,Portfolio,Team,PortfolioCategory)) 
