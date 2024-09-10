from django import forms
from .models import Dish
from restaurants.models import Restaurant


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = (
            "restaurant",
            "name",
            "description",
            "price",
            "category",
            "photo",
            "availability",
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(DishForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["restaurant"].queryset = Restaurant.objects.filter(user=user)

    def clean(self):
        name = self.cleaned_data["name"]
        dish_name_exists = Dish.objects.filter(name__iexact=name).exists()
        if dish_name_exists:
            self.add_error("name", "Ya existe el nombre de restaurant")

        return self.cleaned_data
