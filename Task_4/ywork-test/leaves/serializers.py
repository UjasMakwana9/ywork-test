from rest_framework import serializers
from .models import LeaveRecord

class LeaveRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRecord
        fields = ['id', 'employee', 'month', 'no_of_leaves']