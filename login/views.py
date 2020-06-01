from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def user_login(request):
    """Authenticate a user."""
    # Etape 1 :
    username = request.POST["username"]
    password = request.POST["password"]

    # Etape 2 :
    user = authenticate(request, username=username, password=password)

    # Etape 3 :
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Vous êtes connecté !")
    else:
        messages.add_message(
            request, messages.ERROR, "Les champs renseignés sont invalides."
        )

    return redirect("home")


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Vous êtes déconnecté !")
    return redirect("home")


def auth_user(request):
    return render(request, 'login/login.html')
