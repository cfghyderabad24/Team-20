from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Admin,Farmer,FarmerFields


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

def farmerlogin(request):
    if request.method == "POST":
        return checkfarmerlogin(request)
    return render(request, "farmerlogin.html")

# Create your views here.
@login_required
def farmerhome(request):
    funame = request.session["funame"]
    return render(request,"farmerhome.html",{"farmeruname":funame})
def farmerlogout(request):
    request.session.flush()  # This will clear all session data
    return redirect('farmerlogin')  # Redirect to the login page after logging out


def checkfarmerlogin(request):
    farmeruname=request.POST["uname"] #uname given in html page
    farmerpwd=request.POST["pwd"]

    flag=Farmer.objects.filter(Q(username=farmeruname)&Q(password=farmerpwd)) # Q Query, comparing the models username and the data from the adminlogin post (adminuname)
    print(flag)

    if flag:
        request.session["funame"]=farmeruname #for creating session for adminuname
        return render(request,"farmerhome.html",{"farmeruname":farmeruname})
    else:
        #return HttpResponse("Login Failed")
        msg="Login Failed"
        return render(request,"farmerlogin.html",{"message":msg})




def farmer_form(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        pincode = request.POST.get('pincode')
        gender = request.POST.get('gender')
        aadhar_number = request.POST.get('aadhar_number')
        contact_number = request.POST.get('contact_number')
        area_ploughed = request.POST.get('area_ploughed')
        season = request.POST.get('season')
        crops_grown = request.POST.get('crops_grown')
        seeds_used = request.POST.get('seeds_used')
        date_of_seed_sown = request.POST.get('date_of_seed_sown')
        transplanting = request.POST.get('transplanting')
        irrigation_method = request.POST.get('irrigation_method')
        fertilisers_used = request.POST.get('fertilisers_used')
        date_of_harvesting = request.POST.get('date_of_harvesting')
        yield_in_kg = request.POST.get('yield')
        financial_need = request.POST.get('financial_need')

        # Save data to the database
        farmer = FarmerFields(
            name=name,
            pincode=pincode,
            gender=gender,
            aadhar_number=aadhar_number,
            contact_number=contact_number,
            area_ploughed=area_ploughed,
            season=season,
            crops_grown=crops_grown,
            seeds_used=seeds_used,
            date_of_seed_sown=date_of_seed_sown,
            transplanting=transplanting,
            irrigation_method=irrigation_method,
            fertilisers_used=fertilisers_used,
            date_of_harvesting=date_of_harvesting,
            yield_in_kg=yield_in_kg,
            financial_need=financial_need
        )
        farmer.save()

        return HttpResponse("Form submitted successfully!")
    return render(request, 'farmer_form.html')