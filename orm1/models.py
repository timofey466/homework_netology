from django.db import models


class Phone(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

