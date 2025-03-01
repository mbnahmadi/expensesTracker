from django.shortcuts import render
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


User = get_user_model()

# class RegisterUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer

#     def get_token(self, serializer):
#         user = serializer.save()

#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)

#         response_data = {
#             'user': {
#                 'id': user.id,
#                 'email': user.email,
#                 'first_name': user.first_name,
#                 'last_name': user.last_name,
#                 'username': user.username
#             },
#             'refresh': str(refresh),
#             'access_token': access_token
#         }
#         return Response(response_data, status=status.HTTP_201_CREATED)

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(request_body=UserRegisterSerializer)
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username
            },
            'refresh': str(refresh),
            'access_token': str(refresh.access_token)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








