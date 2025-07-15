from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(b"Hello, Seenode. You're at the top of the world.")
