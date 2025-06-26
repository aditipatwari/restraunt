from django.urls import path
from .models import *
from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [

    path('get_page/',get_page),
    path('login_view/',login_view),
    path('userRegister/',createUser),
    path('get/<int:pk>/',DishesListCreateView.as_view(),name=""),
    path('get_registerform/',get_registerform,name="get_registerform"),
    path('get_loginform/',get_loginform,name="get_loginform"),
    path('home/',get_home,name="home"),
    path('logout/',get_logout,name="logout"),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/hello/', hello_view, name='hello_api'),
    path('get_form/',get_form,name="get_form"),
    path('get_table/',get_table,name="table"),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair')
]