from django.shortcuts import render
from .models import WeightLog
from .forms import WeightForm
from django.shortcuts import render, redirect, get_object_or_404

def metrics_view(request):
    weight_logs = WeightLog.objects.filter(user=request.user).order_by('date_logged')
    dates = [log.date_logged.strftime("%Y-%m-%d") for log in weight_logs]
    weights = [log.weight for log in weight_logs]

    context = {
        'dates': dates,
        'weights': weights,
    }

    return render(request, 'metrics/user_metrics.html', context)

def new_weight(request):
    if request.method == 'POST':
        form = WeightForm(request.POST)
        if form.is_valid():
            new_weight = form.save(commit=False)
            new_weight.user = request.user
            new_weight.save()
            return redirect('metrics')
        else:
            return render(request, 'metrics/new_weight.html', {'form': form})
    else:
        form = WeightForm()
        return render(request, 'metrics/new_weight.html', {'form': form})