# Generated by Django 4.2.5 on 2023-10-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_gyminfo_established_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gyminfo',
            name='year_established',
            field=models.PositiveIntegerField(default=2022),
        ),
    ]
