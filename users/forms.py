from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ("Estudiante", "Estudiante"),
        ("Restaurant", "Restaurant"),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        field = [
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

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user_type = self.cleaned_data.get("user_type")

        if user_type == "Estudiante":
            user.is_student = True
        elif user_type == "Restaurant":
            user.is_restaurant = True
        if commit:
            user.save()
        return user
