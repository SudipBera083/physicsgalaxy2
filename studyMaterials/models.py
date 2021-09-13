from django.db import models
# Create your models here.
class pdf(models.Model):
    pdf_name = models.CharField(max_length=50, default="none")
    category = models.CharField(max_length=100,default="none")
    description = models.CharField(max_length=100,default="none")
    pdf = models.FileField(upload_to='studyMaterials/media')

# shwing the product name on the database

    def __str__(self):
         return self.pdf_name
