from django.db import models

# Create your models here.
class TempStat(models.Model):
    year = models.PositiveSmallIntegerField()
    annual_mean = models.DecimalField(max_digits=4, decimal_places=2)
    moving_mean = models.DecimalField(max_digits=4, decimal_places=2) 

    def __str__(self):
        return self.year
