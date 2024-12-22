# Import necessary modules
from django.contrib import admin  # Django admin
from django.urls import path       # URL routing
from authentication.views import * 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving

# Define URL patterns
urlpatterns = [
    path('', home, name="home"),      # Home page
    path("admin/", admin.site.urls),          # Admin interface
    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
]

