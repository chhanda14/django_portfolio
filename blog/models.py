from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title