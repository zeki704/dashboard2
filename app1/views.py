from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.user.is_anonymous:
        return redirect('login')

    return render(request, "index.html")
