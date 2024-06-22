from django.shortcuts import render
from django.http import HttpResponse

def homefunction(request):
    return render(request,"index.html")

def loginfunction(request):
    return render(request,"login.html")