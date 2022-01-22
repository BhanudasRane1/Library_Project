from re import template
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views.generic import View 


# Create your views here.

class Login_View(View):
    def get(self,request):
        template = 'account/login.html'
        return render(request, template)
    def post(self,request):
        template = 'account/login.html'
        try:
            if request.method=='POST':
                username = request.POST.get('username')
                passwordd= request.POST.get('password') 
                user = auth.authenticate(username=username,password=passwordd)
                if user is not None:
                    auth.login(request,user)
                    messages.error(request,'Successfully login')
                    return redirect("/")
                else:
                    messages.error(request,'Invalid credentials....Please Enter valid credentials')
                    return redirect('login')
            else: 
                return render(request, template)
        except:
            return redirect('unauthorized_access_url')


class Signup_View(View):
    def get(self,request):
        template = 'account/signup.html'
        return render(request, template)

    def post(self,request):
        template = 'account/signup.html'
        if request.method == 'POST':
            username=request.POST.get('username')
            first_name=request.POST.get('first_name')
            password1= request.POST.get('password1')
            password2= request.POST.get('password2')
            email = request.POST.get('email')
            
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request,'Username is already taken')
                    return render(request, template)
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.error(request,'Email is already taken')
                    # return redirect('register')
                    return render(request, template)
                else:
                    user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
                    user.save()
                    messages.error(request,'Account created successfully')
                    return render(request, 'account/login.html')
            else:
                messages.error(request,'Please enter same password')
                return render(request, template)
            return redirect('/')
        return render(request, template)

def logout(request):
    auth.logout(request)
    return redirect('/')
      

