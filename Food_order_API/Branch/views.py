from django.shortcuts import render

# Create your views here.
from .serializers import BranchSerializer
from .models import Branch
from rest_framework import generics

class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchCreate(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchRetrieve(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchUpdate(generics.UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDelete(generics.DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
