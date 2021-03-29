from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create_user(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user


# class UserSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

