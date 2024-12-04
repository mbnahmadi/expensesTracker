from django.shortcuts import render
from .serializers import createUserSerializers
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class createUserView(APIView):
    swagger_auto_schema(request_body=createUserSerializers)
    def post(self,request):
        serializer=createUserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user':user})
        return Response(serializer.error)



