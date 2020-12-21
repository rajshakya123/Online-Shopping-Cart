from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def basic(request):
    return render(request,'basic.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        First_name = request.POST.get('fname')
        Last_name =request.POST.get('lname')
        Email = request.POST.get('email')
        password1 =request.POST.get ('password1')
        password2 = request.POST.get('password2')

        #cheks here created



        user = User.objects.create_user(username=username, email=Email, password=password1)
        user.first_name = First_name
        user.last_name = Last_name
        user.save()
        messages.info(request, 'Your account has been successfully created')
        return redirect('index')

    else:
         messages.error(request,"404-Page Not Found")
         return redirect('index')

def handlelogin(request):
		if request.method == 'POST':
			loginusername= request.POST['loginusername']
			loginpassword = request.POST['loginPassword']

			user = auth.authenticate(username=loginusername,password=loginpassword)

			if user is not None:
				auth.login(request,user)
				messages.success(request,"Successfully loged in")
				return redirect('/shop')
			else:
				messages.error(request,"invalid Credentials,please try again")
				return redirect('index')

		return HttpResponse("404-Page Not Found")


def handlelogout(request):
		logout(request)
		messages.success(request,"successfully loged out")
		return redirect('index')
