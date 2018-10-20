from django.db import models

# Create your models here.
class Recognition(models.Model):
    name = models.Charfield(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
