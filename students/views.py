from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from django.http import Http404
from django.contrib import messages


# Create your views here.
def student_update_view(request, pk):
    try:
        restaurant = get_object_or_404(Student, pk=pk, user=request.user)
    except Http404:
        # Handle the error, for example, redirect to an error page or show a custom message
        messages.add_message(
            request,
            messages.INFO,
            "Resulta que eres restaurantero",
        )
        return redirect("landing:home")

    restaurant = get_object_or_404(Student, pk=pk, user=request.user)

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=restaurant,
        )

        if form.is_valid():
            form.save()
            return redirect("restaurants:update", pk=restaurant.pk)
    else:
        form = StudentForm(instance=restaurant)
    return render(
        request, "restaurants/update.html", {"form": form, "restaurant": restaurant}
    )
