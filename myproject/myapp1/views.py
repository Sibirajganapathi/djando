from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
def fun(request):
    return HttpResponse("Hi...welcome")
def function(request,x):
    return HttpResponse("no of cout"+x)
class admiral(View):
    def get(self,request):
        return HttpResponse("sibiraj")
def home(request):
    a={}
    a[]
    return render(request,'simple.html',a)
