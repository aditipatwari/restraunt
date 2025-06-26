from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny  
from .serializers import *

from rest_framework import generics, mixins
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer




# Create your views here.
def get_page(request):
    dishes = Dishes.objects.all()
    paginator = Paginator(dishes,5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context={
        'page_obj':page_obj
    }
    return render(request,'table.html',context)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        # Authentication successful
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        # Authentication failed
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@csrf_exempt
@api_view(['POST'])
def createUser(request):
    print('data',request.data)
    user = User.objects.create_user(username=request.data['username'],email=request.data['email'],password=request.data['password'])
    return JsonResponse({'message': f'User {user.username} created successfully!'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    try:
        username = request.data.get('username')
        print('username:',username)
        # email = request.data.get('email')
        password = request.data.get('password')
        print('password:',password)

        if not username or not password:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({'message': f'User {user.username} created successfully!'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@permission_classes([AllowAny])
class DishesListCreateView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Dishes.objects.all()
    serializer_class = Dishes_serializers

    def get(self, request, *args, **kwargs):  # List
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):  # Create
        return self.create(request, *args, **kwargs)
    
    
@permission_classes([AllowAny])
class DishesListCreateView(ListCreateAPIView):
    queryset = Dishes.objects.all()
    serializer_class = Dishes_serializers


def get_registerform(request):
    if request.method=="POST":
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        CustomUser = get_user_model()

        CustomUser.objects.create_user(username=email,password=password)
    return render(request,'registerform.html')

@csrf_exempt
def get_loginform(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        print(request)
        user = authenticate(request, username=email, password=password)  
        print(user)
        if user is not None:
            print('in condition')
            login(request, user)
            # messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            # messages.error(request, "Invalid email or password.")
            return render(request, 'loginform.html')
    
    return render(request, 'loginform.html') 
    # logout(request)

def get_home(request):
    return render(request,'home.html')

def get_logout(request):
    logout(request)
    return redirect('get_loginform')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hello_view(request):
    return Response("JWT is working!")

def get_form(request):
    if request.method=="POST":
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        age = request.POST.get("age")
        CustomUser = get_user_model()
        CustomUser.objects.create_user(username=username,password=password,age=age)
        
        return redirect('table')
    else:
        return render(request,'form.html')
    
def get_table(request):
    data = CustomUser.objects.all()
    context={
        "data":data
    }
    return render(request,'logintable.html',context)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer