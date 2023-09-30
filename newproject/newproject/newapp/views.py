from django.http import HttpResponse
from django.shortcuts import render
from . models import place,people
# Create your views here.

def demo(request):
    obj=place.objects.all()
    obj1=people.objects.all()
    return render(request,'index.html',{'result':obj,'res':obj1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,'about.html',{'result':res,'subtraction':sub,'product':mul,'division':div})
#
# def contact(request):
#     return HttpResponse("contact details")