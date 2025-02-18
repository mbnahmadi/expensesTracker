from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'first_name', 'last_name', 'email')

    def validate(self, data):
        if len(data['password']) < 8:
            raise serializers.ValidationError('password must be at least 8 character long')
        
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password':'passwords do not match.'})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
        )

        return user


    