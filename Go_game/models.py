import datetime
from bson.objectid import ObjectId
from db_connection import db

# Create your models here.


class Game:
    game_collection = db["games"]

    @staticmethod
    def create(player1, player2, sgf_data):
        """
        Crée une nouvelle partie et l'insère dans la collection de jeux.
        """
        game = {
            'player1': player1,
            'player2': player2,
            'sgf_data': sgf_data,
            'created_at': datetime.datetime.utcnow()
        }
        Game.game_collection.insert_one(game)
        return game

    @staticmethod
    def get(game_id):
        """
        Récupère une partie par son ID.
        """
        return Game.game_collection.find_one({'_id': ObjectId(game_id)})

    @staticmethod
    def list_all():
        """
        Liste toutes les parties enregistrées.
        """
        return Game.game_collection.find()


class Problem:
    collection = db['problemx']

    @staticmethod
    def create(description, black_positions, white_positions, solution, created_by):
        problem = {
            'description': description,
            'black_positions': black_positions,
            'white_positions': white_positions,
            'solution': solution,
            'created_by': created_by,
            'is_approved': False,
            'created_at': datetime.datetime.utcnow()
        }
        Problem.collection.insert_one(problem)
        return problem

    @staticmethod
    def get(problem_id):
        return Problem.collection.find_one({'_id': ObjectId(problem_id)})

    @staticmethod
    def get_all_approved():
        return Problem.collection.find({'is_approved': True})