from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.game_list, name='game_list'),
    path('problems/', views.problem_list, name='problem_list'),

]
