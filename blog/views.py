from django.shortcuts import render
from .models import BlogPost, Tag
from django.views.generic import ListView, DetailView
import random

def blog(request):
    """blog page"""
    return render(request, 'blog/blog.html')

class BlogPostListView(ListView):
    """blog page"""
    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = 'blogposts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        '''mulitple contexts - blogposts & tags'''
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class BlogPostDetailView(DetailView):
    '''Detail View of a single post'''
    model = BlogPost
    context_object_name = 'blogposts'