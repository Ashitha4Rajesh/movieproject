from django.db import models
class Review(models.Model):
    image = models.ImageField(upload_to="books/cover",null=True,blank=True)
    name = models.CharField(max_length=20)
    year= models.IntegerField()
  
# Create your models here.
