from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            nickname = validated_data['nickname'],
            age = validated_data['age'],
            password = validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['username','nickname','age','password']