from django.db import models

# Create your models here.
class Link(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else 'Unnamed Link'
