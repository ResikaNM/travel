from django.http import HttpResponse
from django.shortcuts import render
from  . models import Place,staff

# Create your views here.
# def demo(request):
#     name="india"
#     return render(request, "homehome.html",{'obj':name})
#     # return render(request,"home.html")
#     #return HttpResponse('hello world')
# def about(request):
#     return HttpResponse('about')
# def contact(request):
#     return render(request,"contact.html")
# def details(request):
#     return HttpResponse('details')
# def thanks(request):
#     return render(request,"thanks.html")
# def addition(request):
#     return render(request,"addition.html")
# def addresult(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     aadd=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#
#     return render(request,"addresult.html",{'ans1':aadd,'ans2':sub,'ans3':mul,'ans4':div})




def statc(request):
    obj1=Place.objects.all()
    obj2=staff.objects.all()

    return render(request,"index.html",{'result':obj1,'result1':obj2})

