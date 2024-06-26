# Generated by Django 5.0.4 on 2024-05-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0015_alter_personaldates_weekdays'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldates',
            name='weekdays',
        ),
        migrations.AddField(
            model_name='personaldates',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personaldates',
            name='monday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personaldates',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personaldates',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personaldates',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personaldates',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personaldates',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]
