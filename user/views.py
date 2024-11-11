from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from movie.models import movieDetails


# Create your views here.
def userRegistration(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        firstName=request.POST.get('firstname')
        lastName=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                print(User.objects.filter(username=username))
                print("dhfdgfdj")
                messages.error(request,"username already exist")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"this email already exist")
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=firstName,last_name=lastName, username=username,email=email,password=password)
                messages.success(request, "Profile successfully created.")
                return redirect('login')
        else:
            messages.error(request, " password not match.")
    return render(request,'userreg.html')

def loginpage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.is_staff:
                return redirect('adminmovielist')
            else:
                return redirect('home')
        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')

def updateprofile(request):
    user=request.user
    if request.method=='POST':
        username=request.POST.get('username')
        firstName=request.POST.get('firstname')
        lastName=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            if User.objects.filter(username=username).exclude(username=user.username).exists():
                messages.error(request,"username already exist")
                return redirect('updateprofile')
            elif User.objects.filter(email=email).exclude(username=user.email).exists():
                messages.error(request,"this email already exist")
                return redirect('updateprofile')
            else:
                user.first_name=firstName
                user.last_name=lastName
                user.username=username
                user.email=email
                user.password=password
                user.save()
                # messages.success(request, "Profile successfully created.")
                return redirect('login')
        else:
            messages.error(request, "password not match.")
    return render(request,'userProfileEdit.html',{'user':user})


def home(request):
    return render(request,'home.html')
def dashbord(request):
    user=request.user
    movies=movieDetails.objects.filter(user=user)
    return render(request,'dashboard.html',{'movies':movies})