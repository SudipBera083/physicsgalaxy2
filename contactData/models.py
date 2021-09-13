from django.db import models


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=50, default="none")
    email = models.CharField(max_length=50, default="none")
    date = models.CharField(max_length=50, default="none")
    comments = models.CharField(max_length=100,default="none")

# shwing the product name on the database

    def __str__(self):
         return self.name
