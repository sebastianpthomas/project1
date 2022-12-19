from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    return render(request,'accounts/register.html',{'form':form})

def login(request):
    return render(request, 'accounts/new.html')

def new(request):
    return render(request, 'accounts/new.html')
