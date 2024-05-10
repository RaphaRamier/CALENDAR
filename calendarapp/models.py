from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class FamilyEvent(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True
    )

    start_at = models.DateTimeField(

    )

    end_at = models.DateTimeField(

    )

    is_active = models.BooleanField(
        default=True
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='user_event'
    )

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(max_length=200)

    event = models.ForeignKey(
        FamilyEvent,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='event')

    description = models.TextField(
        blank=False,
        null=False
    )

    is_active = models.BooleanField(
        default=True
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='user_task'
    )

    def __str__(self):
        return str(self.name)
