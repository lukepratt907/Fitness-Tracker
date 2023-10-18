from django.contrib import admin
from .models import PerformanceMetric

class PerformanceMetricAdmin(admin.ModelAdmin):
    pass

admin.site.register(PerformanceMetric, PerformanceMetricAdmin)
