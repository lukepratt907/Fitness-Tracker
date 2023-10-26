from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout, Exercise
from .forms import WorkoutForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View

@login_required
def workout_page(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            form.save_exercises()  # Add this line to save related exercises
            return redirect('workout_page')
    else:
        form = WorkoutForm()

    workouts = Workout.objects.filter(user=request.user)

    return render(request, 'workouts/workout_page.html', {'form': form, 'workouts': workouts})

@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    workout.delete()
    return redirect('workout_page')

class ExerciseAutocompleteView(View):
    @login_required
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term', '')
        exercises = Exercise.objects.filter(name__icontains=term).values_list('name', flat=True)
        return JsonResponse(list(exercises), safe=False)