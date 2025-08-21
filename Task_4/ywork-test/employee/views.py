from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from datetime import datetime

class EmployeeCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeBaseSalaryUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    def get_object(self):
        return super().get_object()
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class HighEarnersAPIView(APIView):
    def get(self, request, department):
        # Get top 3 unique base salaries in the department
        top_salaries = (
            Employee.objects.filter(department=department)
            .order_by('-baseSalary')
            .values_list('baseSalary', flat=True)
            .distinct()
        )
        top_salaries = list(dict.fromkeys(top_salaries))[:3]  # Ensure uniqueness and top 3

        # Get employees with those salaries
        high_earners = Employee.objects.filter(
            department=department,
            baseSalary__in=top_salaries
        )
        serializer = EmployeeSerializer(high_earners, many=True)
        return Response(serializer.data)

class HighEarnersByMonthAPIView(APIView):
    def get(self, request, department, month):
        try:
            # Parse the month string into a date object
            month_date = datetime.strptime(month, "%Y-%m-%d").date().replace(day=1)
        except Exception:
            return Response({'error': 'Invalid month format, use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

        # Get top 3 unique base salaries in the department for the given month
        top_salaries = (
            Employee.objects.filter(department=department)
            .order_by('-baseSalary')
            .values_list('baseSalary', flat=True)
            .distinct()
        )
        top_salaries = list(dict.fromkeys(top_salaries))[:3]  # Ensure uniqueness and top 3

        # Get employees with those salaries
        high_earners = Employee.objects.filter(
            department=department,
            baseSalary__in=top_salaries
        )
        serializer = EmployeeSerializer(high_earners, many=True)
        return Response(serializer.data)


