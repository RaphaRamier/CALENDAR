from datetime import datetime
from django.db import models


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
        auto_now_add=True
        )
    
    end_at = models.DateTimeField(
        auto_now_add=True
        )
    is_active = models.BooleanField(
        default=True
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
        related_name='user'
    )

    event = models.ForeignKey(
        FamilyEvent,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='user')

    description = models.TextField(
        blank=False,
        null=False
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return str(self.name)