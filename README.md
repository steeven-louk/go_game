# Plateforme de Jeu de Go



## Table des matières

- [Introduction](#introduction)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)


## Introduction

La Plateforme de Jeu de Go est un projet visant à fournir une interface en ligne pour jouer au jeu de go, résoudre des problèmes (tsumego), et accéder à des parties de joueurs professionnels annotées. L'objectif principal est de promouvoir et de faciliter l'apprentissage du jeu de go grâce à une plateforme interactive et éducative.

## Prérequis

Pour pouvoir installer et exécuter ce projet, vous aurez besoin des éléments suivants :

- Python 3.x
- Django 3.x
- MySQL
- Django-bootstrap5

## Installation

Pour installer et configurer l'environnement de développement nécessaire :

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/steeven-louk/go_game.git
   cd go_game

2. **Installer les dépendances :**
   
   ```bash
   pip install -r requirements.txt

3. **Configurer la base de données :**

- Assurez-vous que MySQL est installé et fonctionne.

- Configurez les paramètres de la base de données dans settings.py :

   ```bash
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'nom_de_la_base_de_donnees',
           'USER': 'nom_utilisateur_mysql',
           'PASSWORD': 'mot_de_passe_mysql',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
  
4. **Chargement des Données Initiales :**
   ```bash
   python manage.py import_problems './Go_game/static/data/problems.json'

5. **Effectuer les migrations initiales :**
   ```bash
   python manage.py makemigrations
   python manage.py migrate


## Utilisation
Pour utiliser l'application :

1. **Démarrer le serveur de développement :**
   ```bash
   python manage.py runserver

2. **Accéder à l'application :**
Ouvrez votre navigateur web et accédez à http://127.0.0.1:8000/.

