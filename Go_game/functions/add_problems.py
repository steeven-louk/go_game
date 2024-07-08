# add_problems.py

import json

import pymongo
from pymongo import MongoClient


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_problems_to_db(problems, db):
    problems_collection = db['problemx']
    problems_collection.insert_many(problems)


def main():
    urls = "mongodb+srv://steevenlouksl:projet_ecole@ecole-projet.wjo1dwf.mongodb.net/"
    client = pymongo.MongoClient(urls)
    db = client['go_game']

    problems = load_json_file('../static/data/problems.json')
    print("problemes loaded", problems)
    save_problems_to_db(problems, db)
    print("Successfully added problems to the database.")


if __name__ == '__main__':
    main()
