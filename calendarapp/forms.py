from datetime import datetime

from django import forms
from django.forms import ModelForm
from calendarapp.models import User, FamilyEvent, Task


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateEventForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        label='Event',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Event'
            }
        )
    )
    description = forms.CharField(
        label='Insert the description.',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'placeholder': "Event's description"
            }
        )
    )
    user = forms.ModelChoiceField(
        User.objects.all(),
        label='User'
    )
    start_at = forms.DateTimeField(
        label='Start at',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local'
            }
        )
    )
    end_at = forms.DateTimeField(
        label='End at',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local'
            }
        )
    )


class CreateTaskForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        label='Task',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': "Task"
            }
        )
    )
    description = forms.CharField(
        label='Insert the description.',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'placeholder': "Task's description"
            }
        )
    )
    user = forms.ModelChoiceField(
        User.objects.all(),
        label='User'
    )

    event = forms.ModelChoiceField(
        FamilyEvent.objects.all(),
        label='Event'
    )
