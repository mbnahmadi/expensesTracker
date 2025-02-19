from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import ExpenseModel
from .serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


User = get_user_model()

class ListExpecesView(generics.ListAPIView):
    queryset = ExpenseModel.objects.all()
    serializer_class = ExpenseSerializer


class CreateExpenseView(generics.CreateAPIView):
    queryset = ExpenseModel.objects.all()
    serializer_class = ExpenseSerializer     
    permission_classes = [IsAuthenticated]