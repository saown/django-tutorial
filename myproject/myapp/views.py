from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('ok it working')

# Create your views here.
