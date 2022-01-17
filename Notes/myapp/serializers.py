from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'created_date', 'modified_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'Notes']


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': ' password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(email=self.validated_data['email']
                    , first_name=self.validated_data['first_name']
                    , last_name=self.validated_data['last_name']
                    , username=self.validated_data['username'])
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password fields': 'passwords must match!'})

        user.set_password(password)
        user.save()
        return user
