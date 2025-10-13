from rest_framework import serializers
from django.contrib.auth import authenticate 
from  .models import User
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model=User
        fields = ['username' , 'email' , 'password' , 'password2' ,'bio']

    def validate(self,attrs):
        if attrs['password']!= attrs['password2']:
            raise serializers.ValidationError({"password": "password fields didn't match."})
        return attrs

    def create(self,validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password.validated_data['password'],
            bio=validated_data.get['bio' "  ")
        )
        return user
class UserLoginSerializer(serializers.Serializer):
    username=attrs('username')
    password=attrs('password') 

    if username and password :
        authenticate(username=username,password=password)
        if not user  :
           raise Serializer.ValidationError('Invalid crdentials')
        attrs['user'] = user 
        return attrs
    raise Serializer.ValidationError('must include "username" and "password"
