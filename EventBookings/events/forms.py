from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CategoryForm(forms.ModelForm):
    
    class Meta():
        model = Category
        fields =['name',]

class SubCategoryForm(forms.ModelForm):
    
    class Meta():
        model = Sub_category
        fields =['name', 'category',]

class LocationForm(forms.ModelForm):

    class Meta():
        model = Location
        fields = ['city', 'country', 'street', 'street_num', 'capacity',]

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('dob', 'events')

        widgets = {
                'dob': forms.DateInput(attrs={'type': 'date'}),
            }

    events = forms.ModelMultipleChoiceField(
        queryset=Event.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class EventForm(forms.ModelForm):
    
    class Meta():
        model = Event
        fields =['title', 'date', 'duration', 'likes', 'image', 'sub_category', 'location', ]
        
        widgets = {
                'date': forms.DateInput(attrs={'type': 'date'}),
            }

