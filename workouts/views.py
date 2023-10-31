# workouts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, CustomWorkout
from .forms import WorkoutForm, CustomWorkoutForm

@login_required
def create_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'workouts/create_workout.html', {'form': form})

@login_required
def create_custom_workout(request):
    if request.method == 'POST':
        title = request.POST.get('Title', False)
        description = request.POST.get('Description', False)
        category = request.POST.get('Category', False)#not working right?
        w = CustomWorkout(user=request.user, title=title, description=description, category=category)
        w.save()
        return redirect('workout_list')

    else:
        form = CustomWorkoutForm()
        return render(request, 'workouts/create_custom_workout.html', {
            'form': form

        })

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)

    if request.method == 'POST':
        # Delete the workout
        workout.delete()
        return redirect('workout_list')  # Replace with the actual URL name for the workout list

    # Redirect to the workout list if the request is not a POST
    return redirect('workout_list')  # Replace with the actual URL name for the workout list