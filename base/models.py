from django.db import models
from django.utils.text import slugify

from PIL import Image

class Tag(models.Model):
    '''Project Tags'''
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProjectStatus(models.Model):
    '''Current status of project'''
    status = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Project Statuses"

    def __str__(self):
        return self.status

# Create your models here.
class ProjectPost(models.Model):
    '''Fields for a single portfolio post'''

    # Thumbnail
    title = models.CharField(max_length=200, blank=False)
    sub_heading = models.CharField(max_length=150, null=True, blank=False)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="images/placeholder.png")
    
    active = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    
    # Project Post Details
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=True)
    
    problem = models.TextField(null=True, blank=True)
    objective = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    challenge = models.TextField(null=True, blank=True)
    mistake = models.TextField(null=True, blank=True)
    enjoyed = models.TextField(null=True, blank=True)
    leadership = models.TextField(null=True, blank=True)
    possible_revisions = models.TextField(null=True, blank=True)

    # Side Bar
    github_link = models.URLField(max_length=200, null=True, blank=True)
    web_link = models.URLField(max_length=200, null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    project_status = models.ManyToManyField(ProjectStatus, blank=False)
    tags = models.ManyToManyField(Tag, blank=False)

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

class ProjectPostImage(models.Model):
    '''Field for project images'''
    post = models.ForeignKey(ProjectPost, default="images/placeholder.png", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="images/")
    caption = models.CharField(max_length=200, default="Picture" , blank=False)

    def __str__(self):
        return self.post.title

# class BlogPost():