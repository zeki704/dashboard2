from django.db import models


class Auto(models.Model):
    name = models.CharField(max_length=128)
    dav_raqami = models.CharField(max_length=50)
    rangi = models.CharField(max_length=50)
    yili = models.CharField(max_length=20)

    def __str__(self):
        return self.name
