from django.db import models
from django.utils.text import slugify

from PIL import Image

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProjectStatus(models.Model):
    status = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Project Statuses"

    def __str__(self):
        return self.status

# Create your models here.
class ProjectPost(models.Model):
    '''Fields for a single portfolio post'''

    # Decided not to include file uploads, would rather have them as static files

    # Facade
    title = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200, null=True, blank=True) # can have none
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="images/placeholder.png")
    active = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    
    # Project Post Details (DetailView?)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    # ongoing = models.BooleanField(default=False)   ?boolean for ongoing?
    problem = models.TextField(null=True, blank=True)
    objective = models.TextField(null=True, blank=True)
    builtwith = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project_status = models.ManyToManyField(ProjectStatus, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # creates hyphenated urls for project posts
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = ProjectPost.objects.filter(slug=slug).exists()
            count = 1
            # corrects for identical urls to make it unique
            # adds a number at the end
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count) 
                has_slug = ProjectPost.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
# class BlogPost():