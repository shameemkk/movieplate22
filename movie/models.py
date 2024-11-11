from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class movieDetails(models.Model):
    poster=models.ImageField(upload_to='media/')
    title=models.CharField(max_length=100)
    releaseDate=models.DateField()
    director=models.CharField(max_length=100)
    actors=models.CharField(max_length=100)
    rating=models.FloatField()
    description=models.CharField(max_length=250)
    youTubeLink=models.CharField(max_length=150)
    type=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='movie')
