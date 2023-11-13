from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app1.models import User


def sign_in(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email']).first()
        if not user:
            return render(request, "auth/index.html", {"error": "User yoki parol xato"})
        if not user.check_password(data['pass']):
            return render(request, "auth/index.html", {"error": "User yoki parol xato"})
        if not user.is_active:
            return render(request, "auth/index.html", {"error": "Bunaqa user yo'q"})
        print("salom2\n\n")

        login(request, user)
        print("salo3m\n\n")
        return redirect('home')

    return render(request, "auth/index.html")


def sign_up(request):

    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email=data['email']).first()
        if user:
            return render(request, "auth/index.html", {"error": "Email band"})

        user = User.objects.create_user(email=data['email'],
                                        password=data['pass'],
                                        name=data['name'],
                                        familiya=data['lastname'])
        authenticate(request)
        login(request, user)
        return redirect('home')

    return render(request, "auth/index.html")


@login_required(login_url="login")
def sign_out(request):
    logout(request)
    return redirect("login")
