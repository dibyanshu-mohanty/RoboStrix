from django.db import models

class Dash(models.Model):
    temp=models.FloatField(default=True)
    vib=models.BooleanField(default=True)
    hum=models.IntegerField(default=0)
    flam=models.IntegerField(default=0)
    intru=models.BooleanField(default=True)
    inc=models.BooleanField(default=True)

    def __str__(self):
        return self.name
