from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    Created_on = models.DateTimeField(default= datetime.now, blank=True)
    action = models.CharField(max_length = 200)

    def _str__(self):
        return f"{self.title} is {self.text}"