from importlib.resources import contents
from re import template
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Produto


def index(request):
    prods = Produto.objects.all()
    context = {
        "curso": "Programação Web com Django Framework",
        "desc": "Lorem ipsum dolor sit amet, que quom ismai casade.",
        "produtos": prods
    }
    return render(request, "index.html", context)


def contato(request):
    return render(request, "contato.html")


def produto(request, pk):
    prod = get_object_or_404(Produto, id=pk)
    context = {
        "produto": prod
    }
    return render(request, "produto.html", context)

