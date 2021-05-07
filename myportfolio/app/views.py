from django.shortcuts import render,redirect
from .models import contact

# Create your views here.
def touch(request):
    if request.method == 'POST':
        obj = contact(Name=request.POST["Name"],
                      Email=request.POST["Email"],
                      Subject=request.POST["Subject"],
                      Message=request.POST["Message"])
        obj.save()
        return redirect('/')
    else:
        return render(request,'index.html')