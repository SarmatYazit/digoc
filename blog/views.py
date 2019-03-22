from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')

def contakty(request):
    return render(request,'blog/contakty.html')
