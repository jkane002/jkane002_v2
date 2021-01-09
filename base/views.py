from django.shortcuts import render, redirect

from .models import ProjectPost, ProjectPostImage
from django.views.generic import ListView

from django.urls import reverse
from django.http import JsonResponse

# Tutoring Page
import stripe
import os
stripe.api_key = os.environ.get('STRIPE_TEST_SK')

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

def project_post_carousel(request, slug):
    '''Renders only the post's image carousel'''
    post = ProjectPost.objects.get(slug=slug)
    photos = ProjectPostImage.objects.filter(post=post)
    context = { 
        'post':post,
        'photos':photos
    } 
    return render(request, 'base/projectscarousel.html', context)

def tutor(request):
    """tutor page"""
    return render(request, 'base/tutor.html')

def charge(request):
    amount = 5

    if request.method == 'POST':
        print('Data: ', request.POST)

        customer = stripe.Customer.create(
			name=request.POST['name'],
			email=request.POST['email'],
			source=request.POST['stripeToken']
			)

        charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="Tutoring"
			)
        
    return redirect(reverse('tutor-success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'base/tutor_success.html', {'amount':amount})