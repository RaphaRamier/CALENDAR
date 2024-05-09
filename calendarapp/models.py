from datetime import datetime
from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


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
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(max_length=200)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='username'
    )

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

    def __str__(self):
        return str(self.name)
