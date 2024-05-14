from django.db import models


class Cards(models.Model):
    idCard = models.IntegerField()
    title = models.TextField()
    desc = models.TextField()
    img = models.TextField()
    cost = models.IntegerField()
