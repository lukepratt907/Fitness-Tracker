from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, UserRegisterForm, DiaryForm, ReminderForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DiaryEntry, Reminder
from django.views.decorators.cache import cache_control
from django.db.models import Q
from .forms import LoginForm, UserRegisterForm, DiaryForm, GoalForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import DiaryEntry, Goal
import logging

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# View to allow user registraton and check for valid submission and password declaration
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users-login')
        else:
            messages.error(request, 'Invalid Submission')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# View to allow user login and check for valid submission and password declaration
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, form.get_user())
                return redirect('users-profile')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')

        else:
            messages.error(request, 'Invalid username or password. Please try again.')


    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

# View for access to user profile
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

# View for logging out of the user's account
def logout_view(request):
    logout(request)
    return redirect('/')

# View for listing all diary entries including pagination
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def diary_list(request):
    diaries = DiaryEntry.objects.filter(user=request.user).order_by('-date')
    search = request.GET.get('search', '')
    if search:
        diaries = diaries.filter(
            Q(content__icontains=search) |
            Q(title__icontains=search) |
            Q(date__icontains=search)
        )

    p = Paginator(diaries, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'users/diary.html', {'page_obj': page_obj, 'search': search})

# View for diary detail additions
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def diary_detail(request, pk):
    diary_entry = get_object_or_404(DiaryEntry, pk=pk)
    return render(request, 'users/diary_detail.html', {'diary_entry': diary_entry})

# View for creating a diary entry and checking if form is valid
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_diary_entry(request):
    logger = logging.getLogger(__name__)
    logger.debug(request.POST)
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary_entry = form.save(commit=False)
            diary_entry.user = request.user
            diary_entry.save()
            return redirect('users-diary')
        else:
            logger.error(f"Form Errors: {form.errors}")
            return render(request, 'users/diary_entry.html', {'form': form})
    else:
        logger.error("Invalid request type")
        form = DiaryForm()
        return render(request, 'users/diary_entry.html', {'form': form})

# View for updating existing diaries
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_diary_entry(request, pk):
    diary_entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary_entry)
        if form.is_valid():
            form.save()
            return redirect('diary-detail', pk=diary_entry.pk)
    else:
        form = DiaryForm(instance=diary_entry)
    return render(request, 'users/update_diary_entry.html', {'form': form, 'diary_entry': diary_entry})

# View for deleting diary entries
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_diary_entry(request, pk):
    diary_entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == "POST":
        diary_entry.delete()
        return redirect('users-diary')
    return render(request, 'users/delete_diary_entry.html', {'diary_entry': diary_entry})

# View for access to the user's goals
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def goal_view(request):
    goals = Goal.objects.filter(user=request.user).order_by('end_date')
    search = request.GET.get('search', '')
    if search:
        goals = goals.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(start_date__icontains=search) |
            Q(end_date__icontains=search) |
            Q(status__icontains=search)
        )
    p = Paginator(goals, 6)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'users/goals.html', {'search': search, 'page_obj': page_obj})

# View of specific goal details
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    return render(request, 'users/goal_detail.html', {'goal': goal})

# View for creating new goal entries
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_goal(request):
    logger = logging.getLogger(__name__)
    logger.debug(request.POST)
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            new_goal = form.save(commit=False)
            new_goal.user = request.user
            new_goal.save()
            return redirect('users-goal')
        else:
            logger.error(f"Form Errors: {form.errors}")
            return render(request, 'users/new_goal.html', {'form': form})
    else:
        logger.error("Invalid request type")
        form = GoalForm()
        return render(request, 'users/new_goal.html', {'form': form})

# View for update exising goals
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal-detail', pk=goal.pk)
    else:
        form = GoalForm(instance=goal)
    return render(request, 'users/update_goal.html', {'form': form, 'goal': goal})

# View for deleting goals
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == "POST":
        goal.delete()
        return redirect('users-goal')
    return render(request, 'users/delete_goal.html', {'goal': goal})

# View for accessing the email reminder functionality
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def reminder_view(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect('users-reminder')
        else:
            return redirect('users-reminder')
    else:
        reminders = Reminder.objects.filter(user=request.user)
        form = ReminderForm()
        return render(request, 'users/reminder.html', {'user': request.user, 'reminders': reminders, 'form': form})