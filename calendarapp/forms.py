from datetime import datetime
from django.utils import timezone
from django import forms
from django.forms import ModelForm
from calendarapp.models import FamilyEvent, Task, PersonalDates
from django.contrib.auth.models import User

users = User.objects.all()

# Crie a lista de escolhas (choices)
choices = [(str(user.id), user.username) for user in users]


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = FamilyEvent
        fields = ['name', 'description', 'crew', 'start_at', 'end_at']
        exclude = ['is_active', ]
        labels = {
            'name': 'Event name',
            'description': 'Event description',
            'start_at': 'Start date',
            'end_at': 'End date',
            'crew': 'Member'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_at': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_at': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'crew': forms.SelectMultiple(attrs={'class': 'form-control'}, choices=choices)
        }

    def clean(self):
        cleaned_data = super().clean()
        start_at = cleaned_data.get('start_at')
        end_at = cleaned_data.get('end_at')

        if start_at and end_at:
            if start_at > end_at:
                raise forms.ValidationError("Event cannot start after end date")

        if start_at and start_at < timezone.now():
            raise forms.ValidationError("Start date cannot be in the past")

        if end_at and end_at < timezone.now():
            raise forms.ValidationError("End date cannot be in the past")

        return cleaned_data


class CreateAdminTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['is_active', ]
        labels = {
            'name': 'Name',
            'event': 'Event',
            'description': 'Description',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.SelectMultiple(attrs={'class': 'form-control'}, choices=choices)

        }


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['is_active', 'user']
        labels = {
            'name': 'Name',
            'event': 'Event',
            'description': 'Description',
        }

        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
        }
