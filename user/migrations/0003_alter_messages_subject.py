# Generated by Django 5.0.4 on 2024-05-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_messages_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='subject',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]