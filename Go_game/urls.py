from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.game_list, name='game_list'),
    path('problems/', views.problem_list, name='problem_list'),
    path('problems/<int:problem_id>/', views.problem_detail, name='problem_detail'), # Route pour les détails des problèmes
    path('auth/register/', views.register, name='register'),  # Route pour l'enregistrement
    path('auth/login/', views.login_view, name='login'),  # Route pour la connexion
    path('auth/logout/', views.user_logout, name='logout'),  # Route pour la deconnexion

]
