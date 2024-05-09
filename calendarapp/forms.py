from datetime import datetime

from django import forms
from django.forms import ModelForm
from calendarapp.models import User, FamilyEvent, Task


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = FamilyEvent
        exclude = ['is_active', ]
        labels = {
            'name': 'Event name',
            'description': 'Event description',
            'start_at': 'Start date',
            'end_at': 'End date',
            'user': 'User'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_at': forms.DateInput(format='%d/%m/%Y',
                                        attrs={'type': 'date',
                                               'class': 'form-control'

                                               }
                                        ),
            'end_at': forms.DateInput(format='%d/%m/%Y',
                                      attrs={'type': 'date',
                                             'class': 'form-control'

                                             }
                                      ),
            'user': forms.Select(attrs={'class': 'form-control'})

        }


class CreateTaskForm(forms.ModelForm):
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
            'user': forms.Select(attrs={'class': 'form-control'})
        }
