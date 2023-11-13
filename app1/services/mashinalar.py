from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app1.forms.mashina import Mashinaform
from app1.models import Auto

@login_required(login_url='login')
def get(request, pk=None):
    if pk:
        root = Auto.objects.filter(id=pk).first()
        if not root:
            return redirect("mashina")
        return render(request, "mashinalar/detail.html", {"root": root})

    ctx = {
        "auto": Auto.objects.all()
    }
    return render(request, "mashinalar/list.html", ctx)


def delete1(request, pk):
    try:
        Auto.objects.filter(id=pk).first().delete()
    except:
        pass
    return redirect("mashina")

def addmash(request):
    form = Mashinaform(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("mashina")
    else:
        print(form)

    ctx = {"form": form}

    return render(request, "mashinalar/forms.html", ctx)

def editmash(request, pk):
    try:
        root = Auto.objects.get(id=pk)
    except:
        return redirect("mashina")

    if request.POST:
        forms = Mashinaform(request.POST, request.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect("mashina_det", pk=root.id)
        else:
            print(forms.errors)

    form = Mashinaform(instance=root)
    ctx = {"form": form}

    return render(request, "mashinalar/forms.html", ctx)
