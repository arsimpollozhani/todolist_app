from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)  #populate form with data from the user input (dictionary)    

        if form.is_valid():
            form.save()  #save user
        
        return redirect("/login")
            
    else:
        form = RegisterForm() # otherwise create blank form

    
    return render(request, "register/register.html", {"form" : form})