from django.db import models
from django.contrib.auth.models import User


class ImageOCRecord(models.Model):
    image_path = models.CharField(max_length=255)
    text_from_image = models.TextField(max_length=1000)

    def __str__(self):
        return self.text_from_image
