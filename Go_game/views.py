from django.shortcuts import render,get_object_or_404

from Go_game.models import Problem


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def game_list(request):
    return render(request, 'game_list/index.html')


def problem_list(request):
    problem = Problem.get_all_approved()
    return render(request, 'problem_list/index.html', {'problems': problem})


def problem_detail(request, problem_id):
    problem = Problem.get_problem(problem_id)

    print("problem details",problem)
    return render(request, 'problem_list/problem_detail.html', {'problems': problem})