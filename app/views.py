from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class CategoryView(ModelViewSet):
    serializer_class=BookCategorySerializer
    queryset=BooksCategory.objects.all()

class AdminBookView(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]
    serializer_class=BookSerializer
    queryset=Books.objects.all()

class SignupView(ModelViewSet):
    serializer_class=SignupSerializer
    queryset=User.objects.filter(is_superuser=False,is_staff=False)
    
class LoginView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class StudentView(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    http_method_names=['get']
    serializer_class=BookSerializer
    queryset=Books.objects.all()