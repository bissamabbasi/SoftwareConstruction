from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def loginuser(request):
    err = False
    if request.method == 'POST':
       form = AuthenticationForm(request, data=request.POST)
       if form.is_valid():
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(username=username , password=password)
         if user is not None:
            login(request,user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("/")

       err = True
    form = AuthenticationForm()
    return render(request, 'login/login.html', context={
        "login_form":form, "err":err
    })