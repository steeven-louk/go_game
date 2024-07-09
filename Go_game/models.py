from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1_games')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2_games')
    sgf_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Problem(models.Model):
    black_positions = models.JSONField()
    white_positions = models.JSONField()
    message = models.TextField()
    solution = models.JSONField()
    winning_player = models.CharField(max_length=10)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)