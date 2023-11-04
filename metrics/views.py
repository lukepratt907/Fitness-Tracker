from django.shortcuts import render

# Create your views here.
def metrics_view(request):
    return render(request, 'metrics/user_metrics.html')