from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def pricing_view(request):
    return render(request, 'pricing.html')

def cars_view(request):
    return render(request, 'car.html')

def blog_view(request):
    return render(request, 'blog.html')

from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'contact.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page
        else:
            # Authentication failed, display an error message
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html')
