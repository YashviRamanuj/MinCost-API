from django.db import models

class Order(models.Model):
    qA = models.FloatField(blank=True, default=0)  # quantity of item A in the order
    qB = models.FloatField(blank=True, default=0)
    qC = models.FloatField(blank=True, default=0)
    qD = models.FloatField(blank=True, default=0)
    qE = models.FloatField(blank=True, default=0)
    qF = models.FloatField(blank=True, default=0)
    qG = models.FloatField(blank=True, default=0)
    qH = models.FloatField(blank=True, default=0)
    qI = models.FloatField(blank=True, default=0)
