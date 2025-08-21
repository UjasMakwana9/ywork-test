from django.db import models
from employee.models import Employee
# Create your models here.
class LeaveRecord(models.Model):
    id = models.AutoField
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    no_of_leaves = models.PositiveIntegerField()

    @property
    def payable_salary(self):
        base_salary = self.employee.baseSalary
        return base_salary - (self.no_of_leaves * (base_salary / 25))