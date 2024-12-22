from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('datetime', views.current_datetime, name='current_datetime'),
]
