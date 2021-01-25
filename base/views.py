from django.shortcuts import render, redirect
from django.conf import settings

from .models import ProjectPost, ProjectPostImage
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse
from django.http import JsonResponse

# Tutoring Page
import stripe
stripe.api_key = settings.STRIPE_SK

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
def charge(request, args):
    '''Stripe charge process'''

    # Dictionary containing Price IDs & payment modes
    price_list = {
       "1weeks" : {
            "price_id" : settings.FULL_1_WEEK,
            "mode" : "payment"   
        },
       "5weeks" : {
            "price_id" : settings.FULL_5_WEEKS,
            "mode" : "payment"   
        },
        "10weeks" : {
            "price_id" : settings.FULL_10_WEEKS,
            "mode" : "payment"
        },
        "15weeks" : {
            "price_id" : settings.FULL_15_WEEKS,
            "mode" : "payment"
        },
        "20weeks" : {
            "price_id" : settings.FULL_20_WEEKS,
            "mode" : "payment"
        },
        # TODO: Figure out subscriptions 
        # "5weeks_Weekly" : {
        #     "price_id" : settings.WEEKLY_SUB,
        #     "mode" : "subscription"
        # }, 
    }
    session = stripe.checkout.Session.create(
        success_url=request.build_absolute_uri(reverse('tutor-success')) + '?success_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('tutor-page')),
        payment_method_types=["card"],
        line_items=[
            {
                "price": price_list[args]["price_id"],
                "quantity": 1,
            },
        ],
        mode=price_list[args]["mode"],
    )
   
    return JsonResponse({
        'session_id' : session.id,
        'STRIPE_PK': settings.STRIPE_PK
    })

def successMsg(request):
    '''Presents a success/thank you message'''
    return render(request, 'base/tutor_success.html')

# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     event = None

#     try:
#         event = stripe.Event.construct_from(
#             json.loads(payload), stripe.api_key
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)

#     # Handle the event
#     if event.type == 'payment_intent.succeeded':
#         payment_intent = event.data.object # contains a stripe.PaymentIntent
#         # Then define and call a method to handle the successful payment intent.
#         # handle_payment_intent_succeeded(payment_intent)
#     elif event.type == 'payment_method.attached':
#         payment_method = event.data.object # contains a stripe.PaymentMethod
#         # Then define and call a method to handle the successful attachment of a PaymentMethod.
#         # handle_payment_method_attached(payment_method)
#         # ... handle other event types
#     else:
#         print('Unhandled event type {}'.format(event.type))

#     return HttpResponse(status=200)