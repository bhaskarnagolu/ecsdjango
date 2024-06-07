from django.shortcuts import render
from django.http import HttpResponse
from .models import Name

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        Name.objects.create(name=name)
    names=Name.objects.all()
    return render(request,"one.html",{'names':names})
