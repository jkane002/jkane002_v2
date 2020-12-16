from django.urls import path, include
from . import views
from .views import ProjectsPostListView

urlpatterns = [
    # path('', views.projects, name='projects-page'),
    path('', ProjectsPostListView.as_view(), name='projects-page'),
    path('post/<slug:slug>/', views.project_post, name='project-post-page'),
    path('about/', views.about, name='about-page'),
    path('blog/', views.blog, name='blog-page'),
]