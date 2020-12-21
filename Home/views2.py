from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User,auth



def index(request):
	return render(request,'index.html')


def signup(request):
	if request.method == 'POST':
		Username = request.POST['username']
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']


		myuser = User.objects.create_user(username=Username, email=email ,password=pass1)
		myuser.first_name = fname
		myuser.last_name = lname
		myuser=User.save(commit=False)
		myuser.save()
		print('user created')
		f = signUp(first_name=First_name, last_name=Last_name, email=Email)
		f.save()
		print('handlesignup')
		messages.success(request,'Your account has been successfully created')
		return redirect('index')

	else:
		return HttpResponse('404-Page Not Found')

def handlelogin(request):
		if request.method == 'POST':
			loginusername= request.POST['username']
			loginpassword = request.POST['password']
			user = authenticate(username=loginusername,password=loginpassword)
			if user is not None:
				login(request,user)
				messages.success(request,"Successfully loged in")
				return redirect('shop')
			else:
				messages.error(request,"invalid Credentials,please try again")
				return redirect('index')

		return render(request,"login.html")
def handlelogout(request):
		logout(request)
		messages.success(request,"successfully loged out")
		return redirect('home')

def login(request,templates='index.html'):
    page_title= 'login'
    if request.method == 'POST':
        postdata = request.POST.copy()
        username = postdata.get('loginusername','')
        password = postdata.get('loginPassword','')


        try:
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.info(request, 'Your account has been successfully login')
            return redirect('/shop')

        except:
            error = True


    else:
        return HttpResponse("404-error")
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        First_name = request.POST.get('fname')
        Last_name =request.POST.get('lname')
        Email = request.POST.get('email')
        password1 =request.POST.get ('password1')
        password2 = request.POST.get('password2')

        #cheks here created


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'already Signup')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,'already Signup')
            else:
                user = User.objects.create_user(username=username, email=Email, password=password1)
                user.first_name = First_name
                user.last_name = Last_name
                user.save()
                messages.info(request, 'Your account has been successfully created')
                return redirect('index')
                user=authenticate(username=username,password=password1)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Successfully loged in")
                    return redirect('/shop')
        else:
            print('password not match')
    else:
         messages.error(request,"404-Page Not Found")
         return redirect('index')