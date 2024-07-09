import json

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404, redirect
from Go_game.functions.add_problems import convert_coordinates
from Go_game.models import Problem
from django.contrib.auth.models import User


# Create your views here.
@login_required
def index(request):
    return render(request, 'home/index.html')


def game_list(request):
    return render(request, 'game_list/index.html')


def problem_list(request):
    problem = Problem.objects.all()
    return render(request, 'problem_list/index.html', {'problems': problem})


def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    black_positions = convert_coordinates(problem.black_positions)
    white_positions = convert_coordinates(problem.white_positions)
    solution = convert_coordinates([move[1] for move in problem.solution])
    print("solution", solution)
    return render(request, 'problem_list/problem_detail.html', {
        'problem': problem,
        'black_positions': json.dumps(black_positions),
        'white_positions': json.dumps(white_positions),
        'solution': json.dumps(solution)
    })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        hashed_password = make_password(password)
        User.objects.create(username=username, password=hashed_password, email=email)
        return redirect('login')
    return render(request, 'register/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/index.html', {'error': 'Invalid credentials'})
    return render(request, 'login/index.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
