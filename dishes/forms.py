from django import forms
from .models import Dish
from restaurants.models import Restaurant


class DishForm(forms.ModelForm):
    CATEGORY = (
        ("DULCE", "DULCE"),
        ("SALADO", "SALADO"),
        ("CALIENTE", "CALIENTE"),
        ("FRIO", "FRIO"),
        ("BEBIDA", "BEBIDA"),
    )

    DISH_AVAILABILITY = (
        ("Si", "Si"),
        ("Agotado", "Agotado"),
    )
    forms.ModelChoiceField(queryset=Restaurant.objects.none())
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    price = forms.DecimalField()
    category = forms.ChoiceField(choices=CATEGORY)
    photo = (forms.ImageField(),)
    availability = forms.ChoiceField(choices=DISH_AVAILABILITY)

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
