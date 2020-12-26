from django.shortcuts import render

from .models import ProjectPost, ProjectPostImage
from django.views.generic import ListView

class ProjectsPostListView(ListView):
    """Projects page (home)"""
    model = ProjectPost
    template_name = 'base/projects.html'
    context_object_name = 'posts'
    ordering = ['-start_date']
    paginate_by = 3

def project_post(request, slug):
    '''A single project post with a slug ID & URL'''
    post = ProjectPost.objects.get(slug=slug)
    photos = ProjectPostImage.objects.filter(post=post)
    context = { 
        'post':post,
        'photos':photos
    } 
    return render(request, 'base/projectpost.html', context)

def about(request):
    """about page"""
    # context = {'posts': Post.objects.all()}
    return render(request, 'base/about.html')

def blog(request):
    """blog page"""
    # context = {'posts': Post.objects.all()}
    return render(request, 'base/blog.html')

def project_post_carousel(request, slug):
    '''Renders only the post's image carousel'''
    post = ProjectPost.objects.get(slug=slug)
    photos = ProjectPostImage.objects.filter(post=post)
    context = { 
        'post':post,
        'photos':photos
    } 
    return render(request, 'base/projectscarousel.html', context)