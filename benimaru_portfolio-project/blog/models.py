from django.db import models

class Blog(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    