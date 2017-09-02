from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.

def index(req):
    print(" request was ",req);
    return HttpResponse("Hello There!");
