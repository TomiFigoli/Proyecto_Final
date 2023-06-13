from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import forms


# Create your views here.
def index(request):
    return render(request, "home/index.html")

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html", {"messages": "Vendedor creado 👌"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})    