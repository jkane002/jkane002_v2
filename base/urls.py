from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projects, name='projects-page'),
    path('post/<slug:slug>/', views.project_post, name='project-post-page'),
    path('about/', views.about, name='about-page'),
    path('blog/', views.blog, name='blog-page'),
]