# workouts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, Exercise, WorkoutExercise
from .forms import WorkoutForm, WorkoutExerciseFormSet
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.cache import cache_control


@login_required(login_url='users/login.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_workout(request):
    if request.method == 'POST' and 'btnlog' in request.POST:
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
    elif request.method == 'POST' and 'btnlogsave' in request.POST:
            option = request.POST.get('actualvalue')# value of this is none
            #return HttpResponse(option)
            obj = get_object_or_404(Workout, id=option)
            #new_obj = Workout.objects.get(id=option)
            exs_list = obj.workoutexercise_set.all()# this is good
            #return HttpResponse(exs_list)
            new_workout_instance = Workout.objects.create(
                user = obj.user,
                name = obj.name,
                description = obj.description
            )
            new_relation_instances = []
            for e in exs_list:
                #return HttpResponse(e.sets)
                new_exs = Exercise.objects.create(name=e.exercise.name)
                #return HttpResponse(e.sets)
                new_relation_instance = WorkoutExercise(
                    workout = new_workout_instance,
                    exercise = new_exs,
                    sets = e.sets,
                    reps = e.reps
                )
                new_relation_instances.append(new_relation_instance)
            WorkoutExercise.objects.bulk_create(new_relation_instances)
            return redirect('workout_list')
    else:
        form = WorkoutForm()
        exercise_formset = WorkoutExerciseFormSet(instance=Workout())
        objectlist = Workout.objects.distinct()
    return render(request, 'workouts/create_workout.html', {'form': form, "exercise_formset": exercise_formset, 'objectlist': objectlist})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)

    if request.method == 'POST':
        # Delete the workout
        workout.delete()
        return redirect('workout_list')  # Replace with the actual URL name for the workout list

    # Redirect to the workout list if the request is not a POST
    return redirect('workout_list')  # Replace with the actual URL name for the workout list