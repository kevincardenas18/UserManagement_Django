from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def singup(request):

    if request.method == 'GET':
        return render(request, 'singup.html', {
        'form' : UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #Register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('welcome')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form' : UserCreationForm,
                    'error': 'El usuario ya existe'
                    }) 
        return render(request, 'singup.html', {
                      'form' : UserCreationForm,
                      'error': 'Las contrasseñas no son iguales'
                      }) 
@login_required
def singout(request):
    logout(request)
    return redirect('home')

@login_required
def welcome(request, user_id):
    #user = User.objects.get(id=user_id)
    #print(user.id)
    return render(request, 'welcome.html')    

def singin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})
        login(request, user)
        return redirect('welcome',user_id=user.id)

        
