# Generated by Django 4.1.2 on 2023-11-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryentry',
            name='title',
            field=models.CharField(default='Diary Entry', max_length=100),
        ),
    ]