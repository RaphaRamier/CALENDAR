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
        fields = ['birthday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        labels={
            'birthday': 'Birthday',
            'monday': 'Monday',
            'tuesday': 'Tuesday',
            'wednesday': 'Wednesday',
            'thursday': 'Thursday',
            'friday': 'Friday',
            'saturday': 'Saturday',
            'sunday': 'Sunday',

        }

        widgets={
            'birthday': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'monday': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tuesday': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'wednesday': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'thursday': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'friday': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'saturday': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sunday': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


