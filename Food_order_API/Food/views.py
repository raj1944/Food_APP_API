from django.shortcuts import render

# Create your views here.
from .serializers import FoodSerializer, MenuSerializer
from .models import Food, Menu
from rest_framework import generics

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodCreate(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodRetrieve(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodUpdate(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDelete(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuCreate(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuRetrieve(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuUpdate(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDelete(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer