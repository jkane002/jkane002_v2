from django.shortcuts import render, redirect
from django.conf import settings

from .models import ProjectPost, ProjectPostImage
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse
from django.http import JsonResponse

# Tutoring Page
import stripe
stripe.api_key = settings.STRIPE_TEST_SK

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

# ok to redirect to Stripe
@csrf_exempt
def charge(request):
    '''Stripe charge process'''
    session = stripe.checkout.Session.create(
        success_url=request.build_absolute_uri(reverse('tutor-success')) + '?success_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('tutor-page')),
        payment_method_types=["card"],
        line_items=[
            {
                "price": "price_1I8HMjI1xA2AfvmHJHZoD403",
                "quantity": 1,
            },
        ],
        mode="payment",
    )
   
    return JsonResponse({
        'session_id' : session.id,
        'STRIPE_TEST_PK': settings.STRIPE_TEST_PK
    })

def successMsg(request):
    '''Presents a success/thank you message'''
    return render(request, 'base/tutor_success.html')