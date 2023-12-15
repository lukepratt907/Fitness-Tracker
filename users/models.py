from django.db import models
from django.contrib.auth.models import User

GOAL_STATUS = (
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
)

# Model for user information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user}\'s Profile'

# Model for user's diary information
class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, default="Diary Entry")
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Diary entries"
    
    def __str__(self):
        return f'{self.user}s Diary ({self.date})'

# Model for user's goal information
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Goal")
    description = models.TextField(blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=GOAL_STATUS, max_length=50, default="in_progress")

    def __str__(self):
        return f'{self.user}s Goals'

# Model for user's reminder information
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    message = models.TextField(max_length=1000)
    time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f'{self.user}s Reminders'