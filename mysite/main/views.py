from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import ToDoList, Item

# Create your views here.

def index(request, id):
    lista = get_object_or_404(ToDoList, id=id)
    my_dict = {"name" : lista.name}
    return render(request, "main/list.html", {"lista": lista})


def home (request):
    return render(request, "main/home.html")