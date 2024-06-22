from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Admin


def login(request):
    if request.method == "POST":
        return checkadminlogin(request)
    return render(request, "login.html")

# Create your views here.
@login_required
def adminhome(request):
    auname = request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})
def logout(request):
    request.session.flush()  # This will clear all session data
    return redirect('login')  # Redirect to the login page after logging out


def checkadminlogin(request):
    adminuname=request.POST["uname"] #uname given in html page
    adminpwd=request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd)) # Q Query, comparing the models username and the data from the adminlogin post (adminuname)
    print(flag)

    if flag:
        request.session["auname"]=adminuname #for creating session for adminuname
        return render(request,"adminhome.html",{"adminuname":adminuname})
    else:
        #return HttpResponse("Login Failed")
        msg="Login Failed"
        return render(request,"login.html",{"message":msg})

@login_required
def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})

@login_required
def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("Old Pwd is Correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        msg="Password Updated Successfully"
    else:
        print("Old Password is Incorrect")
        msg="Old Password is Incorrect"
    return render(request,"adminchangepwd.html",{"adminuname":auname,"message":msg})

