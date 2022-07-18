from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name='edit'),
    path('editEvent/<int:pk>', views.edit_event, name='edit_event'),
    path('editSubCategory/<int:pk>', views.edit_sub_category, name='edit_sub_category'),
    path('editLocation/<int:pk>', views.edit_location, name='edit_location'),
    path('book/<int:pk>', views.book_view, name='book_event'),
    path('like/<int:pk>', views.like_view, name='like_event'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)