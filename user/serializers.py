from rest_framework import serializers
from .models import CustomUser


class createUserSerializers(serializers.ModelSerializer):
    model=CustomUser
    fields='__all__'