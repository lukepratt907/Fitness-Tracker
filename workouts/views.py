# workouts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, CustomWorkout
from .forms import WorkoutForm, CustomWorkoutForm, WorkoutExerciseFormSet

@login_required
def create_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        exercise_formset = WorkoutExerciseFormSet(request.POST, instance=Workout())
        if form.is_valid() and exercise_formset.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()

            # Save the related WorkflowExercise instances with the workout instance
            instances = exercise_formset.save(commit=False)
            for instance in instances:
                instance.workout = workout
                instance.save()

            return redirect('workout_list')
    else:
        form = WorkoutForm()
        exercise_formset = WorkoutExerciseFormSet(instance=Workout())
    return render(request, 'workouts/create_workout.html', {'form': form, "exercise_formset": exercise_formset})

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