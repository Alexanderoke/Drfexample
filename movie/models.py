from django.db import models

# Create your models here.

class Movie(models.Model):
  movie_name= models.CharField(max_length=50)
  movie_image= models.ImageField(upload_to='movie/images')
  movie_description=models.CharField(max_length=1000)

  def __str__(self):
      return self.name
