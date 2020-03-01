from django.db import models

# Create your models here.


class product(models.Model):
    name= models.CharField(max_length=100, blank=False)
    price= models.IntegerField(blank=False)
    def __str__(self):
        return self.name

