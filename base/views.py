from django.shortcuts import render

from .models import ProjectPost

def projects(request):
    """Projects page (home)"""
    posts = ProjectPost.objects.all()

    context = {'posts': posts }
    return render(request, 'base/projects.html', context)

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

'''
class PostListView(ListView):
    model = Post
    template_name = 'base/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
'''
