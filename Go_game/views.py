from django.shortcuts import render

from Go_game.models import Problem


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def game_list(request):
    return render(request, 'game_list/index.html')


def problem_list(request):
    problem = Problem.get_all_approved()
    print("problem viesw",problem)
    return render(request, 'problem_list/index.html', {'problems': problem})
