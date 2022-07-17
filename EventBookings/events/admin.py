from django.contrib import admin
from .models import *

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'duration', 'image', 'created_at', 'updated_at', 'location', 'sub_category')
    filter_horizontal = ('likes',)
    
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'country', 'street', 'street_num', 'capacity')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'rating', 'event_id', 'user_id')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'dob', 'created_at', 'updated_at')
    filter_horizontal = ('events',)

admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Profile, ProfileAdmin)