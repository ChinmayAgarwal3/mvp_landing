from django.db import models

# Create your models here.
class email_entry(models.Model):
    email=models.EmailField()