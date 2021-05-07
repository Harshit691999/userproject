from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.contrib.auth.models import User  # user is a inbulit model in djagno
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib import messages

# password harshit@691999
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")   
    else:
        print("-------indexed data------")
        print(request)
        print(request.user.username)
        print(request.method)
        print(request.body)
        print(request.path)
        print(request.scheme) 
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            print(user)
            return redirect("/")
        else:
            messages.info(request,"username or password incorrect")
            return render(request,'login.html')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return render(request,'login.html')


# def registeruser(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
#         user.save()
#         print("User have been created")
#         return redirect("/loginuser")
#     else:
#         return render(request,'register.html')

def registeruser(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,"Account has created for"+user_name)
            return redirect("/loginuser")
    context = {'form':form}
    return render(request,'register2.html',context)
