from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
