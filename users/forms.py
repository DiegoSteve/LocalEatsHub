from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label="Alias",
        required=True,
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "id": "username",
            }
        ),
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "id": "email",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={"id": "password"}),
    )

    USER_TYPE_CHOICES = [
        ("Estudiante", "Estudiante"),
        ("Restaurant", "Restaurant"),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password",
            "user_type",
        ]
        exclude = [
            "is_student",
            "is_restaurant",
            "is_active",
            "date_joined",
        ]

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("El username ya se encuentra en uso")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not re.findall("[A-Z]", password):
            raise ValidationError("Debe contener al menos una letra Mayúscula")
        if not re.findall("[a-z]", password):
            raise ValidationError("Debe contener al menos una letra minúscula")
        if not re.findall("[0-9]", password):
            raise ValidationError("Debe contener al menos un dígito numérico")
        if not len(password) >= 8:
            raise ValidationError("Requiere ocho caracteres como mínimo")
        return password

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya se encuentra en uso")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get("user_type")

        if user_type == "Estudiante":
            user.is_student = True
        elif user_type == "Restaurant":
            user.is_restaurant = True
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email",
        required=True,
    )

    password = forms.CharField(
        label="Password",
        required=True,
        initial=None,
        widget=forms.PasswordInput(attrs={"id": "user_password"}),
    )
