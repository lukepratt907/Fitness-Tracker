# Generated by Django 4.2.5 on 2023-10-26 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gyminfo',
            name='established_date',
        ),
    ]
