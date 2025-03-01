from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
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
    


class UpdateExpenseView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=ExpenseSerializer,
        manual_parameters=[
                openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token", type=openapi.TYPE_STRING)
            ])    
    def put(self, request, pk):
        expense = get_object_or_404(ExpenseModel, pk=pk)   # get object at first or get 404 if not found
        self.check_object_permissions(request, expense)    # check user can access to the object if not get forbidden
        
        serializer = ExpenseSerializer(data=request.data, instance=expense)
        if serializer.is_valid():
            save_expense = serializer.save()
            return Response({
                'detail':{
                    'user': save_expense.user.username,
                    'updated_title': save_expense.title,
                    'updated_category': save_expense.category.title,
                    'updated_expense': save_expense.expense,
                    'updated_status': save_expense.status,
                    'updated_updated_at': save_expense.updated_at
                }
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)