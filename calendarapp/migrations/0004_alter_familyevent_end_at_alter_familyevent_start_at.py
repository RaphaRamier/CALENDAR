# Generated by Django 5.0.4 on 2024-05-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_familyevent_user_alter_task_event_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyevent',
            name='end_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='familyevent',
            name='start_at',
            field=models.DateTimeField(),
        ),
    ]
