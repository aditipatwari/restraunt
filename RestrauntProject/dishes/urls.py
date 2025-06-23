from django.urls import path
from .models import *
from .views import *
urlpatterns = [
    path('get_page/',get_page)
]