from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LeaveRecord
from .serializers import LeaveRecordSerializer
from employee.models import Employee

# Create your views here.

class LeaveRecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = LeaveRecord.objects.all()
    serializer_class = LeaveRecordSerializer

class LeaveRecordRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRecord.objects.all()
    serializer_class = LeaveRecordSerializer

from datetime import datetime

class IncreaseLeaveCountPutAPIView(APIView):
    def put(self, request):
        employee_id = request.data.get('employee')
        increment = int(request.data.get('increment', 1))

        try:
            employee = Employee.objects.get(pk=employee_id)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            # Parse full date string
            month_date = datetime.strptime(request.data.get('month'), "%Y-%m-%d").date().replace(day=1)
        except Exception:
            return Response({'error': 'Invalid month format, use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

        leave_record, created = LeaveRecord.objects.get_or_create(
            employee=employee,
            month=month_date,
            defaults={'no_of_leaves': 0}
        )
        leave_record.no_of_leaves += increment
        leave_record.save()
        serializer = LeaveRecordSerializer(leave_record)
        return Response(serializer.data, status=status.HTTP_200_OK)


from datetime import datetime

class PayableSalaryAPIView(APIView):
    def post(self, request):
        employee_id = request.data.get('employee')
        month_str = request.data.get('month')

        try:
            # Parse the string into a date
            month_date = datetime.strptime(month_str, "%Y-%m-%d").date().replace(day=1)
        except Exception:
            return Response({'error': 'Invalid month format, use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            leave_record = LeaveRecord.objects.get(employee_id=employee_id, month=month_date)
            payable_salary = leave_record.payable_salary
        except LeaveRecord.DoesNotExist:
            return Response({'error': 'Leave record not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({
            'employee': employee_id,
            'month': month_date,
            'payable_salary': payable_salary
        }, status=status.HTTP_200_OK)
