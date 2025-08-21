from django.shortcuts import render
from rest_framework import generics
from .models import Department
from .serializers import DepartmentSerializer

# Create your views here.

class DepartmentCreateAPIView(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
