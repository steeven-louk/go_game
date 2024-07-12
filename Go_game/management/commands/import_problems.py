import json
from django.core.management.base import BaseCommand

from Go_game.models import Problem


class Command(BaseCommand):
    help = 'Import problems from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            data = json.load(file)
            for problem_data in data:
                black_positions = problem_data.get("AB", [])
                white_positions = problem_data.get("AW", [])
                #board_size = int(problem_data.get("SZ", 19))
                description = problem_data.get("C", "")
                solution = problem_data.get("SOL", [])

                Problem.objects.create(
                    black_positions=black_positions,
                    white_positions=white_positions,
                    #board_size=board_size,
                    description=description,
                    solution=solution,
                    created_by_id=2222222226666664
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported problems'))
