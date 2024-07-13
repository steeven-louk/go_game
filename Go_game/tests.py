from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Problem, Game
from django.contrib.auth import get_user_model


class ProblemTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(username='testuser', password='password')
        self.user.save()
        self.client.login(username='testuser', password='password')

    def test_create_problem(self):
        problem_data = {
            'black_positions': ["eb", "fb", "bc", "cc", "dc", "be"],
            'white_positions': ["da", "ab", "bb", "cb", "db"],
            'description': 'Black to play: Elementary',
            'solution': [["B", "ba", "Correct.", ""]],
            'created_by_id': 245211555
        }
        problem = Problem.objects.create(**problem_data)
        problem.save()
        problems_count = Problem.objects.count()
        self.assertEqual(problems_count, 1)

    def test_problem_listing(self):
        problem_data = {
            'black_positions': ["eb", "fb", "bc", "cc", "dc", "be"],
            'white_positions': ["da", "ab", "bb", "cb", "db"],
            'description': 'Black to play: Elementary',
            'solution': [["B", "ba", "Correct.", ""]],
            'created_by_id': 245211555

        }
        Problem.objects.create(**problem_data)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Black to play: Elementary')


class GameTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_model = get_user_model()
        self.user1 = self.user_model.objects.create_user(username='testuser1', password='password')
        self.user2 = self.user_model.objects.create_user(username='testuser2', password='password')
        self.user1.save()
        self.user2.save()
        self.client.login(username='testuser1', password='password')

    def test_create_game(self):
        game = Game.objects.create(player1=self.user1, player2=self.user2, sgf_data='(;)')
        game.save()
        games_count = Game.objects.count()
        self.assertEqual(games_count, 1)
