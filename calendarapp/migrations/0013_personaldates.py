# Generated by Django 5.0.4 on 2024-05-15 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0012_alter_task_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('weekdays', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
    ]
