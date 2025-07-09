from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(request, id):
    lista = ToDoList.objects.get(id=id)

    # name : value from html
    # {"save" = ["save"], "c1" = ["clicked"]}

    if request.method == "POST":
        
        print(request.POST) # test

        if request.POST.get("save"):  # name="save" btn   for saving
            
            for item in lista.items.all():  #saving check buttons
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
            
                item.save()
            
        elif request.POST.get("newItem"):   # for new item
            txt = request.POST.get("new")

            if len(txt) > 2:
                lista.items.create(text=txt, complete=False)
            else:
                print("Invalid input")

    return render(request, "main/list.html", {"lista": lista})


def home (request):
    return render(request, "main/home.html", {})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)  # get all info from the form (dict)
        if form.is_valid():
            n = form.cleaned_data["name"]  # get the name from unencrypted data
            t = ToDoList(name=n)
            t.save()
        
        return HttpResponseRedirect ("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(request, "main/create.html", {"form": form})