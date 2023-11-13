from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app1.forms.ishchi import Ishchiform
from app1.models.ishchi import Ishchi



@login_required(login_url='login')
def get_list(request, pk=None):
    if pk:
        root = Ishchi.objects.filter(id=pk).first()
        if not root:
            return redirect("ishchi")
        return render(request, "ishchilar/detail.html", {"root": root})

    ctx = {
        "ishchilar": Ishchi.objects.all()
    }
    return render(request, "ishchilar/list.html", ctx)


def delete(request, pk):
    try:
        Ishchi.objects.filter(id=pk).first().delete()
    except:
        pass
    return redirect("ishchi")

def add(request):
    form = Ishchiform(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("ishchi")
    else:
        print(form)

    ctx = {"form": form}

    return render(request, "ishchilar/forms.html", ctx)

def edit(request, pk):
    try:
        root = Ishchi.objects.get(id=pk)
    except:
        return redirect("ishchi")

    if request.POST:
        forms = Ishchiform(request.POST, request.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect("ishchi_det", pk=root.id)
        else:
            print(forms.errors)

    form = Ishchiform(instance=root)
    ctx = {"form": form}

    return render(request, "ishchilar/forms.html", ctx)


