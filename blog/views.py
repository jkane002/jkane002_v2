from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView, DetailView

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

class BlogPostDetailView(DetailView):
    '''Detail View of a single post'''
    model = BlogPost
    context_object_name = 'blogposts'