from django.urls import path, include
from . import views
from .views import ProjectsPostListView

urlpatterns = [
    path('', ProjectsPostListView.as_view(), name='projects-page'),
    path('post/<slug:slug>/', views.project_post, name='project-post-page'),
    path('post/<slug:slug>/carousel/', views.project_post_carousel , name='project-post-carousel'),
    path('about/', views.about, name='about-page'),
    path('tutor/', views.tutor, name='tutor-page'),
    path('tutor/charge/<str:args>/', views.charge, name='tutor-charge'),
    path('tutor/success/', views.successMsg, name='tutor-success'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook'),
]