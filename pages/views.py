from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>예수사랑교회</h1>")
# Create your views here.
