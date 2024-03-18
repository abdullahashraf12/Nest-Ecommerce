from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForms
from django.contrib import messages
from django.contrib.auth import login, authenticate , logout
from django.conf import settings

User = settings.AUTH_USER_MODEL
def register_user(request):
    if request.method == "POST":
        form = UserRegisterForms(request.POST)
        print("POST Method")
        print(form.is_valid())
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data["username"]
            print(username)
            print("User Created")
            messages.success(request, f"Hey {username}, your account has been created")
            new_user = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password1"])
            login(request, new_user)
            return redirect("core:index")
    else:
        if request.user.is_authenticated:
            return redirect("core:index")
    
        print("GET Request")
        form = UserRegisterForms()

    context = {"form": form}
    
    return render(request, "customer_front_end_ltr/userauth/sign-up.html", context=context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email)
        print(password)
        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request=request,message=f"User with {email} does not exist ")
        user = authenticate(request=request, email=email,password=password)
        if user is not None:
            login(request=request,user=user)
            messages.success(request=request,message="You Are Logged in.")
            return redirect("core:index")
        else:
            messages.warning(request=request,message=f"User Does not Exist ,Create an Account")
    context = {

    }
    return render(request,"customer_front_end_ltr/userauth/sign-in.html", context=context)
def logout_view(request):
    logout(request)
    messages.warning(request,message="User Logout")
    return redirect("userauths:sign-in")