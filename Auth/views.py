from django.shortcuts import render,redirect

# Create your views here.

# required Login 
def home(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request,"Main/home.html")

def log_in(request):
    if request.user.is_authenticated:
        return redirect("/home")
    return render(request,"Auth/login.html")