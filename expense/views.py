from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import ExpenseModel
from .serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.


User = get_user_model()

class ListExpecesView(generics.ListAPIView):
    queryset = ExpenseModel.objects.all()
    serializer_class = ExpenseSerializer


# class CreateExpenseView(generics.CreateAPIView):
#     queryset = ExpenseModel.objects.all()
#     serializer_class = ExpenseSerializer     
#     permission_classes = [IsAuthenticated]


class CreateExpenseView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
            request_body=ExpenseSerializer,
            manual_parameters=[
                openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token", type=openapi.TYPE_STRING)
            ])
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():   #user=request.user
            expense_save = serializer.save()
            return Response({
                'detail':{
                'user': expense_save.user.username,
                'title': expense_save.title,
                'category': expense_save.category.title,
                'expense': expense_save.expense,
                'status': expense_save.status,
                'created_at': expense_save.created_at,
                'updated_at': expense_save.updated_at}
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)