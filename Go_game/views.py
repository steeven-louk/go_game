from django.shortcuts import render

from Go_game.models import Problem
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def game_list(request):
    return render(request, 'game_list/index.html')


def problem_list(request):
    problem = Problem.get_all_approved()
    print("problem viesw",problem)
    return render(request, 'problem_list/index.html', {'problems': problem})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        hashed_password = make_password(password)
        User.objects.create(username=username, password=hashed_password, email=email)
        return redirect('login')
    return render(request, 'register/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login/index.html', {'error': 'Invalid credentials'})
    return render(request, 'login/index.html')