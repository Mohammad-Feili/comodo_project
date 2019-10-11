from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('join-us', views.join_us, name='join-us'),
]
