from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm


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


@login_required
def account(request):

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        
        if "update" in request.POST:
            form = UserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        elif "delete" in request.POST:
            user = request.user
            logout(request)
            user.delete()
            return redirect("login")

    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'register/account.html', {"form": form})