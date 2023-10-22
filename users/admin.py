from django.contrib import admin
from .models import User, UserProfile, DiaryEntry, Goal

class UserProfileAdmin(admin.ModelAdmin):
    pass

class DiaryEntryAdmin(admin.ModelAdmin):
    pass

class GoalAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(DiaryEntry, DiaryEntryAdmin)
admin.site.register(Goal, GoalAdmin)