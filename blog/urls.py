from django.urls import path
from . import views
from .views import (
    BlogPostListView,
    BlogPostDetailView
)

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-page'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
]