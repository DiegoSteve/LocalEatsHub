from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "photo",
            "address",
            "phone",
            "description",
            "delivery_options",
        ]  # Include any fields you want to update
