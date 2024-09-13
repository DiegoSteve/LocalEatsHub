from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Restaurant
from .forms import RestaurantForm
from django.http import Http404
from django.contrib import messages


# Create your views here.
def restaurant_update_view(request, pk):
    try:
        restaurant = get_object_or_404(Restaurant, pk=pk, user=request.user)
    except Http404:
        # Handle the error, for example, redirect to an error page or show a custom message
        messages.add_message(
            request,
            messages.INFO,
            "Resulta que eres Estudiante",
        )
        return redirect("landing:home")

    restaurant = get_object_or_404(Restaurant, pk=pk, user=request.user)

    if request.method == "POST":
        form = RestaurantForm(
            request.POST,
            request.FILES,
            instance=restaurant,
        )

        if form.is_valid():
            form.save()
            return redirect("restaurants:update", pk=restaurant.pk)
    else:
        form = RestaurantForm(instance=restaurant)
    return render(
        request, "restaurants/update.html", {"form": form, "restaurant": restaurant}
    )
