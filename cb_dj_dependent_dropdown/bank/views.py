from django.shortcuts import render, redirect

# Create your views here.
from bank.models import registration, confir


def index(request):
    return render(request,'persons/index.html')

def index2(request):
    return render(request,'persons/index2.html')

def login(request):
    if request.method == 'POST':
        Name1=request.POST.get('Name1',)
        Password=request.POST.get('Password',)

        re = confir(Name1=Name1, Password=Password)
        re.save()

        return redirect('bank:show')
    return render(request, 'persons/login.html')
def register(request):
    if request.method == 'POST':
        Name1=request.POST.get('Name1',)
        Password=request.POST.get('Password',)
        cpassword=request.POST.get('cpassword',)

        reg = registration(Name1=Name1, Password=Password, cpassword=cpassword)
        reg.save()

        return render(request, 'persons/login.html')
    return render(request,'persons/register.html')

def show():

    pass