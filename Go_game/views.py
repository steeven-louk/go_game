import json

from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from Go_game.functions.function import convert_coordinates
from Go_game.models import Problem, User


# Create your views here.

#Affichage de la page d'acceuil nécessite une connexion
@login_required

def index(request):
    return render(request, 'home/index.html')


#Affichage de la page de jeux
@login_required(login_url="login")
def game_list(request):
    return render(request, 'game_list/index.html')


#Recuperation et affichage de la liste des problemes
@login_required(login_url="login")
def problem_list(request):
    problem = Problem.objects.all()
    return render(request, 'problem_list/index.html', {'problems': problem})


#Recuperation d'un probleme
@login_required(login_url="auth/login")
def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    black_positions = convert_coordinates(problem.black_positions)
    white_positions = convert_coordinates(problem.white_positions)
    solution = convert_coordinates([move[1] for move in problem.solution])
    return render(request, 'problem_list/problem_detail.html', {
        'problem': problem,
        'black_positions': json.dumps(black_positions),
        'white_positions': json.dumps(white_positions),
        'solution': json.dumps(solution)
    })


#AUTHENTIFICATION
def register(request):
    error = False
    message = ""
    context = {
        'error': error,
        'message': message,
    }
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        hashed_password = make_password(password)

        try:

            try:
                validate_email(email)
            except:
                error = True
                context.message = "Invalid email address."

            if not error:
                if password != confirm_password:
                    context.error = True
                    context.message = "Invalid password address."
            user = User.objects.filter(email=email).first()

            if user:
                context.error = True
                context.message = "Email address is already in use."

            if not user:
                user = User.objects.create_user(username=username, email=email, password=hashed_password)
                user.save()
                auth_login(request, user)
                return redirect('home')  # Redirige vers la page d'accueil après l'inscription
            context = context.copy()
        except IntegrityError:

            return render(request, 'auth/register/index.html', {'error': context})
    return render(request, 'auth/register/index.html')


def login_view(request):
    error = ""
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = User.objects.filter(email=email).first()

        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                auth_login(request, auth_user)
                return redirect('home')
            else:
                print("password incorrect")
            return redirect('home')
        else:
            print("user does not exist")
            error = "User does not exist"
    return render(request, 'auth/login/index.html', {"error": error})


def user_logout(request):
    #logout(request)
    auth_logout(request)
    return redirect('login')  # Redirige vers la page de connexion après la déconnexion
