from django.conf import settings
from django.core.mail import send_mail

def send_reminder_email(user, reminder):

    send_mail(
        subject='Fitness Tracker Reminder',
        message=reminder.title,
        from_email=settings.EMAIL_FROM,
        recipient_list=[user.email]
    )