from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def login(request):
    print(request)
    return HttpResponse('OK')