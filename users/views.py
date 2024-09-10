from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
)
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("landing:home")  # Redirect after successful registration
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field}:{error}")
    else:
        form = RegistrationForm

    return render(request, "users/registration.html", {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("landing:home")
    form = LoginForm(request=request, data=request.POST)
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            messages.add_message(
                request,
                messages.INFO,
                "Te has conectado correctamente",
            )
            return redirect("landing:home")
        else:
            form = LoginForm()
            return render(
                request,
                "users/login.html",
                {"form": form, "error": "datos incorrectos"},
            )
    else:
        form = LoginForm()
        return render(
            request,
            "users/login.html",
            {"form": form, "error": "datos incorrectos"},
        )


@login_required(login_url="users:login")
def user_logout(request):
    if not request.user.is_authenticated:
        return render(request, "users:login")

    if request.method == "GET":
        logout(request)
        messages.add_message(
            request,
            messages.INFO,
            "Saliste correctamente",
        )
        return redirect("landing:home")

    return render(request, "landing:home")
