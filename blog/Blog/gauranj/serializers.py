from .models import *

from rest_framework import serializers

class  CRUDdataserializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields =(
            "id","name","description"
        )

class CRUDDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CRUDData
        fields = (
            "id", "first_name", "age"
        )


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id", "username", "password"
        )

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["username"],password=validated_data["password"])
        return user


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id", "username", "password"
        )