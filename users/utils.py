from django.conf import settings
from django.core.mail import send_mail

def send_reminder_email(reminder):

    send_mail(
        subject='Fitness Tracker Reminder',
        message=reminder.message,
        from_email=settings.EMAIL_FROM,
        recipient_list=[reminder.user.email]
    )

    print(f"Sent reminder email to {reminder.user.email}")