'''these classes serialized category and expense models'''

from rest_framework import serializers
from django.contrib.auth import get_user_model
from expense.models import CategoryModel, ExpenseModel


User = get_user_model()

class CategorySerialzer(serializers.ModelSerializer):
    '''serialized category model'''
    class Meta:
        '''class Meta'''
        model = CategoryModel
        fields = ('title',)


class ExpenseSerializer(serializers.ModelSerializer):
    '''serialized expense model'''
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        '''class Meta'''
        model = ExpenseModel
        fields = (
            'title', 
            'category', 
            'expense', 
            'status', 
            'created_at', 
            'updated_at'
        )

    def create(self, validated_data):
        '''
        get all validated data from user and save it for each user who is authenticate
        '''
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)    
