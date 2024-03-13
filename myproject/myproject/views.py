#from django.http import HttpResponse

#def homepage(request):
    #return HttpResponse("Hello, Home!")

#def about(request):
    #return HttpResponse("My About")

from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')