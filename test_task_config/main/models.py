from django.db import models


class Weather(models.Model):
    city = models.TextField()
    temperature = models.IntegerField()

    def __str__(self):
        return f"{self.city}: {self.temperature}°C"
