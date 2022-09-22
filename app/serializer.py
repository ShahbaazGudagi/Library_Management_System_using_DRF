from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):   
    class Meta:
        model=User
        fields=[
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
            ]
        extra_kwargs={
            'password':{
                'write_only' : True
            }
        }
    def create(self,validatedData):
        user=User.objects.create(
            username=validatedData['username'],
            first_name=validatedData['first_name'],
            last_name=validatedData['last_name'],
            email=validatedData['email'],
        )   
        user.set_password(validatedData['password']) 
        user.save()
        return user
    
    def update(self,userObject,validatedData):
        if validatedData.get('password'):
            userObject.set_password(validatedData.get('password'))
        userObject.save()
        return validatedData    
    

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BooksCategory
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['id','first_name','last_name','email','username','password']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }

    def create(self,validatedData):
        user = User.objects.create(
            username = validatedData['username'],
            first_name = validatedData['first_name'],
            last_name = validatedData['last_name'],
            email = validatedData['email']
        )
        user.set_password(validatedData['password'])
        user.save() 
        return user 