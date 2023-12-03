from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=128)

class Tasks(models.Model):
    description = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

