from django.http import HttpResponse
from django.shortcuts import render
def create(request):
    if (request.method=='GET'):
        return render(request,'simple.html')
    else:
        n=request.POST['uname']
        e=request.POST['uemail']
        print("Name is",n)
        print("email is",e)
        return HttpResponse("sibi")
