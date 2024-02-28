from django.db import models
from tinymce.models import HTMLField


class Remark(models.Model):
    name = models.CharField(max_length=186)
    description = models.TextField()

    def __str__(self):
        return self.name


class Config(models.Model):
    address = models.CharField(max_length=186)
    phone = models.CharField(max_length=186)
    email = models.CharField(max_length=320)
    logo = models.ImageField(upload_to='images', blank=True)

    # For S.E.O
    author = models.CharField(max_length=186)
    description = models.TextField()
    keywords = models.CharField(max_length=600, help_text="You can seprate them with comma|','")

    # Founder
    founder_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.address}|{self.phone}|{self.email}"

