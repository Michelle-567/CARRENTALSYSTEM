from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('index', views.index, name='index'),  # Make sure this is the root path for the index view
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('cars/', views.cars_view, name='cars'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
]

