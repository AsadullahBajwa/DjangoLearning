from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    blog_file = models.FileField(upload_to='blog_docs')