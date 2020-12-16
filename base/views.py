from django.shortcuts import render

from .models import ProjectPost
from django.views.generic import ListView

# def projects(request):
#     """Projects page (home)"""
#     posts = ProjectPost.objects.all()

#     context = {'posts': posts }
#     return render(request, 'base/projects.html', context)

def project_post(request, slug):
    '''A single project post with a slug ID & URL'''
    post = ProjectPost.objects.get(slug=slug)
    context = { 'post':post } 
    return render(request, 'base/projectpost.html', context)

def about(request):
    """about page"""
    # context = {'posts': Post.objects.all()}
    return render(request, 'base/about.html')

def blog(request):
    """blog page"""
    # context = {'posts': Post.objects.all()}
    return render(request, 'base/blog.html')

class ProjectsPostListView(ListView):
    model = ProjectPost
    template_name = 'base/projects.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 3

