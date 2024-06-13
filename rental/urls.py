from django.urls import path
from . import views

from .views import login_view

urlpatterns = [
    
    path('', login_view, name='login'),
    path('home/', views.index, name='index'),
    path('about/', views.about_view, name='about'),
    path('services.html/', views.services_view, name='services'),
    path('pricing.html/', views.pricing_view, name='pricing'),
    path('cars.html/', views.cars_view, name='cars'),
    path('blog.html/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),

]


    

