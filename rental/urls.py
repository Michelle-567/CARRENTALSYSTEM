from django.urls import path
from . import views

from .views import login_view

urlpatterns = [
    
    path('', login_view, name='login'),
    path('index/', views.index, name='index'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('cars/', views.cars_view, name='cars'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),


    
]

    

