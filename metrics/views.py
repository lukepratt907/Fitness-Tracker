from django.shortcuts import render
from .models import WeightLog
from .forms import WeightForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def metrics_view(request):
    weight_logs = WeightLog.objects.filter(user=request.user).order_by('date_logged')
    dates = [log.date_logged.strftime("%Y-%m-%d") for log in weight_logs]
    weights = [float(log.weight) for log in weight_logs]

    context = {
        'dates': dates,
        'weights': weights,
    }

    return render(request, 'metrics/user_metrics.html', context)

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def weight_list(request):
    weights = WeightLog.objects.filter(user=request.user)
    p = Paginator(weights, 30)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'metrics/edit_weight.html', {'weights': weights, 'page_obj': page_obj})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_weight(request, pk):
    weight_log = get_object_or_404(WeightLog, id=pk, user=request.user)
    if request.method == 'POST':
        form = WeightForm(request.POST, instance=weight_log)
        if form.is_valid():
            form.save()
            return redirect('weight-list')
    else:
        form = WeightForm(instance=weight_log)
    return render(request, 'metrics/edit_weight_form.html', {'form': form, 'weight_log': weight_log})
