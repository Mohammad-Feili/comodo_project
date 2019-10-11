from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('blog/<int:post_id>', views.blog_details, name='blog-details'),
    path('blog-details', views.blog_details, name='blog-details'),
]
