from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    date_published = models.DateField()