from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.game_list, name='game_list'),
    path('problems/', views.problem_list, name='problem_list'),
    path('problems/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
]
