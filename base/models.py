from django.db import models
from PIL import Image

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class ProjectPost(models.Model):
    '''Fields for a single portfolio post'''
    # Facade
    title = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200, null=True, blank=True) # can have none
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="images/placeholder.png")
    # Details (DetailView?)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    # featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    # slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

# class BlogPost():