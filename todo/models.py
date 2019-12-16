from django.db import models
from django.urls import reverse
# Create your models here.
class MyForm(models.Model):
    text = models.TextField(max_length=1000)
    complete = models.BooleanField(default=False)

    
    