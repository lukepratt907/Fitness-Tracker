from django.shortcuts import render
from users.models import UserProfile
from .forms import WeightForm
from django.shortcuts import render, redirect, get_object_or_404

def metrics_view(request):
    return render(request, 'metrics/user_metrics.html')

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