from django.shortcuts import render
from.settings import DEBUG

def rol1(request):
    return render(request, "home.html")

def rol2(request):
    return render(request, "faq.html")

def rol3(request):
    return render(request, "about.html")
