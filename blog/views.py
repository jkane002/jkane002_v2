from django.shortcuts import render

# Create your views here.
def blog(request):
    """blog page"""
    return render(request, 'blog/blog.html')