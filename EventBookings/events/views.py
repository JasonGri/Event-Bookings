from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import *

from utils import *

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

@login_required
def profile(req):
    return render(req, 'events/profile.html')

@staff_member_required
def edit(req):

    logger.info('Loading edit.html')
    if req.method == 'POST':
        logger.info(f'Received POST request: {req.POST}')
        form1 = EventForm(req.POST, prefix='form1')
        form2 = CategoryForm(req.POST, prefix='form2')
        form3 = SubCategoryForm(req.POST, prefix='form3')
        form4 = LocationForm(req.POST, prefix='form4')  

        # if all([form1.is_valid(), form2.is_valid(), form3.is_valid() ,form4.is_valid()]):
        #     form1.save()
        #     form2.save()
        #     form3.save()
        #     form4.save()
        #     return HttpResponseRedirect(reverse('index'))

        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()
        if form3.is_valid():
            form3.save()
        if form4.is_valid():
            form4.save()

        logger.info('Redirecting to main page')
        return HttpResponseRedirect(reverse('index'))

    else:
        form1 = EventForm(prefix='form1')
        form2 = CategoryForm(prefix='form2')
        form3 = SubCategoryForm(prefix='form3')
        form4 = LocationForm(prefix='form4') 

    context = {
    'form1' : form1,
    'form2' : form2,
    'form3' : form3,
    'form4' : form4, 
    }

    
    return render(req, 'events/edit.html', context)