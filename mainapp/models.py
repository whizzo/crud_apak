from django.db import models



class Blog(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()



# Create your models here.
