from django.contrib import admin
from .models import PerformanceMetric, WeightLog

class PerformanceMetricAdmin(admin.ModelAdmin):
    pass

admin.site.register(PerformanceMetric, PerformanceMetricAdmin)
admin.site.register(WeightLog)
