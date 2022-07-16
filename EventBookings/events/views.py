from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import *
from .forms import *

from utils import *

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def index(req):


    context = {
        'events': Event.objects.all(),
        'sub_categories': Sub_category.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(req, 'events/index.html', context)

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

@staff_member_required
def edit(req):

    logger.info('Loading edit.html')
    if req.method == 'POST':
        logger.info(f'Received POST request: {req.POST}')
        form1 = EventForm(req.POST, req.FILES, prefix='form1')
        form2 = CategoryForm(req.POST, prefix='form2')
        form3 = SubCategoryForm(req.POST, prefix='form3')
        form4 = LocationForm(req.POST, prefix='form4')

        if form1.is_valid():
            logger.info('form1 saved')
            form1.save()
        if form2.is_valid():
            logger.info('form2 saved')
            form2.save()
        if form3.is_valid():
            logger.info('form3 saved')
            form3.save()
        if form4.is_valid():
            logger.info('form4 saved')
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
    'events': Event.objects.all(),
    'sub_categories': Sub_category.objects.all(),
    'locations': Location.objects.all(),
    }

    
    return render(req, 'events/edit.html', context)

@login_required
def profile(req):
    logger.info('Loading profile.html')
    if req.method == 'POST':
        logger.info(f'Received POST request: {req.POST}')
        user_form = UserForm(req.POST, instance=req.user)
        profile_form = ProfileForm(req.POST, instance=req.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse(profile))
        logger.error('Error in updating the profile')
    else:
        user_form = UserForm(instance=req.user)
        profile_form = ProfileForm(instance=req.user.profile)


    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(req, 'events/profile.html', context)