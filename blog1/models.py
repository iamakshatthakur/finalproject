from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=225)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    author=models.CharField(max_length=13)
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + 'by' + ' ' + self.author



    
