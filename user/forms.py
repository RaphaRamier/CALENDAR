from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
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
    password = forms.CharField(
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
    username = forms.CharField(
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
    password1 = forms.CharField(
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

    password2 = forms.CharField(
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

    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter your email'
            }
        )
    )
