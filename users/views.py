from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
)

from .forms import RegistrationForm

# Create your views here.


def register(request):
    if request.method == "POST":

        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            messages.success(request, "Cuenta creada exitosamente")
            return redirect("landing:home")
    else:

        form = RegistrationForm()
        return render(
            request,
            "users/registration.html",
            {"form": form, "error": "datos incorrectos"},
        )
