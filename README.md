# Projet 10 -   Créez une API sécurisée RESTful en utilisant Django REST

## Introduction
Ce projet a pour but la création d'une application permettant de remonter et suivre des problèmes techniques (issue tracking system).
L'application permettra aux utilisateurs de créer divers projets, d'ajouter des utilisateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités,
Cette application utilise le framework **Django** + **Django REST framework** ainsi qu'une base de donnée **sqlite3**.

## Installation
####  Cloner ce dépôt : 
```
git clone https://github.com/batshanti/Projet10.git
cd Projet10/
```
####  Créer un environnement virtuel pour le projet :
(Linux or Mac)
```
 python3 -m venv venv
 source venv/bin/activate
```
(Windows)
```
 python -m venv env
 env\Scripts\activate
```
#### Installer les packages :
```
pip install -r requirements.txt
```
#### Démarrer le serveur  :
````
python manage.py runserver
````
#### Documentation de l'API :
https://documenter.getpostman.com/view/22498429/VUr1GYPZ

#### Utilisateur de test : 
| Utilisateur | Mot de passse |
|--|--|
| test_user1 | Password$1 |
| test_user2 | Password$2 |

#### Liste des Endpoints : 
| #   | *Point de terminaison d'API*                                              | *Méthode HTTP* | *URL*       |
|-----|---------------------------------------------------------------------------|----------------|-------------------------------------------|
| 1   | Inscription de l'utilisateur                                              | POST           | /signup/                                  |
| 2   | Connexion de l'utilisateur                                                | POST           | /login/                                   |
| 3   | Récupérer la liste de tous les projets rattachés à l'utilisateur connecté | GET            | /projects/                                |
| 4   | Créer un projet                                                           | POST           | /projects/                                |
| 5   | Récupérer les détails d'un projet via son id                              | GET            | /projects/{id}/                           |
| 6   | Mettre à jour un projet                                                   | PUT            | /projects/{id}/                           |
| 7   | Supprimer un projet et ses problèmes                                      | DELETE         | /projects/{id}/                           |
| 8   | Ajouter un utilisateur (collaborateur) à un projet                        | POST           | /projects/{id}/users/                     |
| 9   | Récupérer la liste de tous les utilisateurs attachés à un projet          | GET            | /projects/{id}/users/                     |
| 10  | Supprimer un utilisateur d'un projet                                      | DELETE         | /projects/{id}/users/{id}/                |
| 11  | Récupérer la liste des problèmes liés à un projet                         | GET            | /projects/{id}/issues/                    |
| 12  | Créer un problème dans un projet                                          | POST           | /projects/{id}/issues/                    |
| 13  | Mettre à jour un problème dans un projet                                  | PUT            | /projects/{id}/issues/{id}               |
| 14  | Supprimer un problème d'un projet                                         | DELETE         | /projects/{id}/issues/{id}               |
| 15  | Créer des commentaires sur un problème                                    | POST           | /projects/{id}/issues/{id}/comments/      |
| 16  | Récupérer la liste de tous les commentaires liés à un problème            | GET            | /projects/{id}/issues/{id}/comments/      |
| 17  | Modifier un commentaire                                                   | PUT            | /projects/{id}/issues/{id}/comments/{id} |
| 18  | Supprimer un commentaire                                                  | DELETE         | /projects/{id}/issues/{id}/comments/{id} |
| 19  | Récupérer un commentaire via son id                                       | GET            | /projects/{id}/issues/{id}/comments/{id} |