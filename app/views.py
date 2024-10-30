from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm , UserAuthenticateForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request,'you have been registred succesfully vow...')
            return redirect('login')
        
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticateForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = UserAuthenticateForm()
    return render(request, 'login.html', {'form': form})
