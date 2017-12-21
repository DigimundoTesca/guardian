from django.db import models

class Trailer(models.Model):

    number = models.PositiveIntegerField()

    def __str__(self):
        return '%s' % self.number


class Delivery(models.Model):

    number = models.PositiveIntegerField()
    trailer = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    units = models.CharField(max_length=10)
    product = models.CharField(max_length=2)
    total = models.PositiveIntegerField()

    def __str__(self):
        return '%s' % self.number