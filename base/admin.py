from django.contrib import admin
from .models import ProjectPost, Tag, ProjectStatus, ProjectPostImage
# Register your models here.

admin.site.register(Tag)
admin.site.register(ProjectStatus)


class ProjectPostImageAdmin(admin.StackedInline):
    '''Image admin'''
    model = ProjectPostImage


@admin.register(ProjectPost)
class ProjectPostAdmin(admin.ModelAdmin):
    '''Registers ProjectPost with inlines of images'''
    inlines = [ProjectPostImageAdmin]

    class Meta:
       model = ProjectPost

@admin.register(ProjectPostImage)
class ProjectPostImageAdmin(admin.ModelAdmin):
    '''Registers Project Post Image admin'''
    pass