from django.db import models
from django.contrib.auth.models import User

METRIC_TYPES = (
    ('personal_record', 'Personal Record'),
    ('bench_press', 'Bench Press'),
    ('squat', 'Squat'),
)

class PerformanceMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric_type = models.CharField(choices=METRIC_TYPES, max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()