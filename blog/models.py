from django.db import models
from django.utils import timezone
from django.urls import reverse

class Tag(models.Model):
    '''Blog Tags'''
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    tags = models.ManyToManyField(Tag, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'pk':self.pk})
