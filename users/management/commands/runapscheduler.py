# runapscheduler.py
import logging

from django.conf import settings
from django.utils import timezone

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from users.models import Reminder
from users.utils import send_reminder_email

logger = logging.getLogger(__name__)


def delete_hanging_reminders():
  """
  Delete any reminders that should have been send and deleted but for some reasons are still in the system
  """
  pass



def send_pending_reminders():
  current_time_minute = timezone.now().replace(second=0).replace(microsecond=0)
  
  pending_reminders = Reminder.objects.filter(
    time__exact=current_time_minute
  )

  print(f"Found {pending_reminders.count()} pending reminders")

  for reminder in pending_reminders:
    send_reminder_email(reminder=reminder)
  
  # Delete the reminders since we already sent them so that they dont take up database space
  pending_reminders.delete()

  # Delete any reminders that should have been send and deleted but for some reasons are still in the system
  Reminder.objects.filter(
    time__lt=current_time_minute
  ).delete()



# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way. 
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
  """
  This job deletes APScheduler job execution entries older than `max_age` from the database.
  It helps to prevent the database from filling up with old historical records that are no
  longer useful.
  
  :param max_age: The maximum length of time to retain historical job execution records.
                  Defaults to 7 days.
  """
  DjangoJobExecution.objects.delete_old_job_executions(max_age) # type: ignore


class Command(BaseCommand):
  help = "Runs APScheduler."

  def handle(self, *args, **options):
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
      send_pending_reminders,
      trigger=CronTrigger(minute="*/1"),  # Every minute
      id="send_pending_reminders",  # The `id` assigned to each job MUST be unique
      max_instances=1,
      replace_existing=True,
    )
    logger.info("Added job 'send_pending_reminders'.")

    scheduler.add_job(
      delete_old_job_executions,
      trigger=CronTrigger(
        day_of_week="mon", hour="00", minute="00"
      ),  # Midnight on Monday, before start of the next work week.
      id="delete_old_job_executions",
      max_instances=1,
      replace_existing=True,
    )
    logger.info(
      "Added weekly job: 'delete_old_job_executions'."
    )

    try:
      logger.info("Starting scheduler...")
      scheduler.start()
    except KeyboardInterrupt:
      logger.info("Stopping scheduler...")
      scheduler.shutdown()
      logger.info("Scheduler shut down successfully!")