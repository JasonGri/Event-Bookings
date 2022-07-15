from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'events/index.html')

def register(req):
    return render(req, 'events/register.html')

def login_view(req):
    return render(req, 'events/login.html')

def logout_view(req):
    pass

def profile(req):
    return render(req, 'events/profile.html')

def edit(req):
    return render(req, 'events/edit.html')