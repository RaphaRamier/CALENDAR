from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from calendarapp.models import PersonalDates


class LoginForm(forms.Form):
    username=forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter your username'
            }
        )
    )
    password=forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Enter your password'
            }
        )
    )


class SignUpForm(forms.Form):
    username=forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter your username'
            }
        )
    )
    password1=forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Enter your password'
            }
        )
    )

    password2=forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Enter your password again'
            }
        )
    )

    email=forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter your email'
            }
        )
    )


class PersonalDateForm(forms.ModelForm):
    class Meta:
        model=PersonalDates
        fields = ['birthday', 'weekdays']
        labels={
            'birthday': 'Birthday',
            'weekdays': 'Weekdays'

        }

        choices_weekday = {
            '0': 'Monday',
            '1': 'Tuesday',
            '2': 'Wednesday',
            '3': 'Thursday',
            '4': 'Friday',
            '5': 'Saturday',
            '6': 'Sunday'
        }

        widgets = {
            'birthday': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'weekdays': forms.SelectMultiple(attrs={'class': 'form-control'}, choices=choices_weekday)
        }


