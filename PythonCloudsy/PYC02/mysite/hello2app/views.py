from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return render(request,"PYC01-HTMLDemo.html")