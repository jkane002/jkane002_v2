from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projects, name='projects-page'),
    path('about/', views.about, name='about-page'),
    path('blog/', views.blog, name='blog-page'),
]