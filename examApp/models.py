from django.db import models


# Create your models here.
class normal_exam(models.Model):
    question= models.CharField(max_length=200, default="none")
    a = models.CharField(max_length=50, default="none")
    b = models.CharField(max_length=50, default="none")
    c = models.CharField(max_length=50, default="none")
    d = models.CharField(max_length=50, default="none")
    currect_ans = models.CharField(max_length=50, default="none")
    

# shwing the product name on the database

    def __str__(self):
         return self.question