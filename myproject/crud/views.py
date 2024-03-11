from django.http import HttpResponse
from django.shortcuts import render

from crud.models import EnquiryForm
def create(request):
    if (request.method=='GET'):
        return render(request,'simple.html')
    else:
        n=request.POST['uname']
        e=request.POST['uemail']
        m=request.POST['umobile']
        print("Name is",n)
        print("email is",e)
        print("mobile is",m)
        EnquiryForm.objects.create(name=n,email=e,mobile=m)
        return HttpResponse("sibi")
