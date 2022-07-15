from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def index(req):
    return render(req, 'events/index.html')

def register(req):
    logger.info('Loading register.html')
    if req.method == "POST":
        logger.info(f'Received POST request: {req.POST}')
        form = UserForm(req.POST)
        
        if form.is_valid():
            user = form.save()
            login(req, user)
            logger.info(f"Registration successful")
            logger.info('Redirecting to profile page')
            return HttpResponseRedirect(reverse('profile'))
        
        else:
            logger.error(f"Unsuccessful registration. Invalid information.")
            return render(req, 'events/register.html', {'message':'Invalid Credentials!'})

    else:
        form = UserForm()

    context = {
        'form':form
    }

    return render(req, 'events/register.html', context)

def login_view(req):
    logger.info('Loading login.html')
    if req.method == 'POST':
        logger.info(f'Received POST request: {req.POST}')
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password= password)

        if user is not None:
            login(req, user)
            logger.info(f"Login successful")
            logger.info('Redirecting to profile page')
            return HttpResponseRedirect(reverse('profile'))
        else:

            logger.error(f"Unsuccessful registration. Invalid information.")
            return render(req, 'events/login.html', {'message':'Invalid Credentials!'})

    else:
        return render(req, 'events/login.html')

def logout_view(req):
    logger.info('Logout initiated')
    logout(req)
    logger.info('Logged out succesfully')
    logger.info('Redirecting to main page')
    return HttpResponseRedirect(reverse(index))

def profile(req):
    return render(req, 'events/profile.html')

def edit(req):
    return render(req, 'events/edit.html')