from django.contrib import admin
from .models import PortfolioPost, Tag
# Register your models here.

admin.site.register(PortfolioPost)
admin.site.register(Tag)