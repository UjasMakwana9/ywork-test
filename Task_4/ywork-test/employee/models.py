from django.db import models
from department.models import Department
# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    baseSalary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name