from django.db import models


class Ishchi(models.Model):
    ism = models.CharField(max_length=128)
    familiya = models.CharField(max_length=128)
    tugilgan_yil = models.DateField()
    lavozimi = models.CharField(max_length=128)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ism} {self.familiya}"
