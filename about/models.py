from django.db import models

class GymInfo(models.Model):
    description = models.TextField()
    year_established = models.PositiveIntegerField(default=2022)

    def __str__(self):
        return f"{self.description} - Established in {self.year_established}"