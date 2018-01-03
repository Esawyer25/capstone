from django.db import models

class Grant(models.Model):
    PI_NAME = models.CharField(max_length=264, null=True)

    def __str__(self):
        return self.PI_NAME # change this to something more sensible later


# Create your models here.
