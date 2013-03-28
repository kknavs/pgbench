from django.db import models


class submitted_measurement(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date of measurement')
    user = models.CharField(max_length=200)
    tags = []
