from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    date_finish = models.DateField()
    date_start = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    descrition = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
