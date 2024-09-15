from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=20)
    duration=models.FloatField()
    rating=models.FloatField()
    typ=models.CharField(max_length=100,default='action')
    image=models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg')

    def __str__(self):
       return self.name