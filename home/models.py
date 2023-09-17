from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")

class Contact(models.Model):
    email = models.CharField(max_length=100 , null=True , blank=True)
    phone_no = models.IntegerField(max_length=10 , null=True , blank=True)
    message = models.TextField(null=True , blank=True)

