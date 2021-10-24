from django.db import models

# Create your models here.
class Image(models.Model):
    images = models.ImageField(upload_to = "img")
    Description = models.CharField(max_length = 100)

    
    def __str__(self):
        return self.Description