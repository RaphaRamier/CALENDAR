# Generated by Django 5.0.4 on 2024-05-10 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0008_alter_task_user_alter_familyevent_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='calendarapp.familyevent'),
        ),
    ]
