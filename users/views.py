from django.shortcuts import render,redirect
from .forms import RigisterForm

def register(request):
    redirect_to=request.POST.get('next',request.GET.get('next',''))
    if request.method=='POST':
        form=RigisterForm(request.POST)
        if form.is_valid():
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form=RigisterForm()
    return render(request,'users/register.html',context={'form':form,'next':redirect_to})

def lead(request):
    return render(request,'lead.html')
# Create your views here.
