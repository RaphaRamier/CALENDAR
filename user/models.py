from django.contrib.auth.models import User
from django.db import models

users=User.objects.all()
choices=[(str(user.id), user.username) for user in users]


class Messages(models.Model):
    sender=models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sender_messages'
    )

    recipients=models.ManyToManyField(
        User,
        related_name='recipient_messages'

    )

    content=models.TextField()

    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        recipients_usernames=", ".join(user.username for user in self.recipients.all())
        return f'Message from {self.sender.username if self.sender else "Unknown"} to {recipients_usernames}'