from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from .models import Dish
from .forms import DishForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from restaurants.models import Restaurant

# Create your views here.


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    template_name = "dishes/add_dish.html"
    # context_object_name = "coin_titles_list"
    form_class = DishForm
    success_url = reverse_lazy("landing:home")
    i_instance = None

    login_url = "users:login"

    def get_form_kwargs(self):
        kwargs = super(DishCreateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        print("USER: ", kwargs["user"])
        return kwargs

    def form_valid(self, form):
        restaurant = form.cleaned_data.get("restaurant")
        print("Restaurant: ", restaurant)
        form.instance.restaurant = restaurant
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)
