from datetime import datetime
from datetime import date
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class FamilyEvent(models.Model):
    id=models.AutoField(
        primary_key=True
    )

    name=models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    description=models.TextField(
        blank=True
    )

    start_at=models.DateTimeField(

    )

    end_at=models.DateTimeField(

    )

    is_active=models.BooleanField(
        default=True
    )

    user=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='user_event'
    )

    crew=models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.name)

    @property
    def days_till(self):
        today=date.today()
        days_till=self.start_at.date() - today
        days_till_stripped=str(days_till).split(",", 1)[0]
        return days_till_stripped


class Task(models.Model):
    id=models.AutoField(
        primary_key=True
    )

    name=models.CharField(max_length=200)

    event=models.ForeignKey(
        FamilyEvent,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='event'
    )

    description=models.TextField(
        blank=False,
        null=False
    )

    is_active=models.BooleanField(
        default=True
    )

    user=models.CharField(
        max_length=200,
        null=True,
        blank=False

    )

    def __str__(self):
        return str(self.name)


class PersonalDates(models.Model):
    birthday=models.DateField(
    )

    weekdays=models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    user=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='user_birthday'
    )

    def __str__(self):
        return str(self.birthday)
