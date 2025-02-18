from django.shortcuts import render
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer





