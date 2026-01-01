from users.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect


# Create your views here.
def main(request):
    return render(request,"users/main.html") 

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            return redirect("users:profile")
        else:
            # return redirect("users:signup")
            context = {
                'form': form
            }
            return render(request, 'users/signup.html', context)
    else:
        form = SignupForm()
        context = {
            "form":form,
        }
        return render(request,"users/signup.html",context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request,user)
            return redirect("users:profile")
        else:
            context = {
                'form': form
            }
            return render(request,"users/login.html",context)
        
    else:
        form = AuthenticationForm()
        context = {
                'form': form
            }
        return render(request,"users/login.html",context)


def logout(request):
    auth.logout(request)
    return redirect("users:main")

@login_required
def profile(request):
    return render(request,"users/profile.html")
