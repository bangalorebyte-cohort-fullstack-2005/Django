from django.db import models

# Create your models here.

class Employee(models.Model):
    Full_name = models.CharField(max_length = 50)
    emp_code = models.IntegerField(max_length = 50)
    mobile = models.IntegerField(max_length = 10)
    Position = models.CharField(max_length = 50)

    def _str_(self):
        return self.Full_name 