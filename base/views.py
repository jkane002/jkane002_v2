from django.shortcuts import render

def projects(request):
    """Projects page (home)"""
    # context = {'posts': Post.objects.all()}
    return render(request, 'base/projects.html')

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
