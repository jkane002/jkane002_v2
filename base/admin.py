from django.contrib import admin
from .models import ProjectPost, Tag, ProjectStatus
# Register your models here.

admin.site.register(ProjectPost)
admin.site.register(Tag)
admin.site.register(ProjectStatus)