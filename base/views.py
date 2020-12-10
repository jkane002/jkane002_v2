from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """base page"""
    # context = {'posts': Post.objects.all()}
    return render(request, 'base/index.html')

'''
class PostListView(ListView):
    model = Post
    template_name = 'base/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
'''
