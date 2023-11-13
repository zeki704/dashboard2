from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from app1.models import User


@staff_member_required(login_url='login')
def get_list(request):
    ctx = {
        "users": User.objects.all()
    }
    return render(request, "ishchilar/user/ss.html", ctx)

@staff_member_required(login_url='login')
def change_perm(requests, pk, status=0):
    user = User.objects.filter(id=pk).first()
    if user and status in [0, 1]:
        user.perm = True if status == 1 else False
        user.save()
    return redirect("user")
