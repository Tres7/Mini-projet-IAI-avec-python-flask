# IAI MINI-PROJET GESTION DES LIVRES D'UNE BIBLIOTHEQUE
# Voici les fonctionnalités
# *GESTION DES LIVRES*
# 1- Lister tous les livres: Cela nous permettra de lister tous les livres présents dans la bibliothèque
Route: /GET/livres
# Résultat de la requête:
 "livres": 
        {
            "Auteur": "Dale Carnegie",
            "Code ISBN": "VGHU",
            "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
            "Editeur": "Haemonies",
            "Titre": "L' art de parler en public",
            "categories_id": 1,
            "id": 7
        },
        {
            "Auteur": "Dale Carnegie",
            "Code ISBN": "VGHU",
            "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
            "Editeur": "Haemonies",
            "Titre": "l'art de parler en public",
            "categories_id": 1,
            "id": 12
        }
# 2 - Modifier un livre: cette fonctionnalité permet de modifier un livre en entrant en utilsant son id
Pour pouvoir faire cette modification, plus besoin d'entrer toutes les références. Il suffira juste d'entrer les références de ce que nous voulons modifier.
route: /PATCH/livres/id
résultat:
{
    "new_book": {
        "Auteur": "Dale Carnegie",
        "Code ISBN": "VGHU",
        "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
        "Editeur": "Haemonies",
        "Titre": "Comment se faire des amis",
        "categories_id": 1,
        "id": 7
    },
    "success": true,
    "updated_book_Id": 7
} 
Conseil: Vérifiez la requête précédente. Vous verrez que le titre du livre a changé
# 3 - Supprimer un livre: Suppression d'un livre juste en entrant son id
route: /DELETE/livres/id
# Résultat de la requête:
"livres": 
        {
            "Auteur": "Dale Carnegie",
            "Code ISBN": "VGHU",
            "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
            "Editeur": "Haemonies",
            "Titre": "l'art de parler en public",
            "categories_id": 1,
            "id": 12
        }
       {
            "Auteur": "Dale Carnegie",
            "Code ISBN": "VGHU",
            "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
            "Editeur": "Haemonies",
            "Titre": "l'art de parler en public",
            "categories_id": 1,
            "id": 13
        }
# 4 - Chercher un livre: Recherche avec son id
route: /GET/livres/id
{
    "researched_Id": 12,
    "researched_book": {
        "Auteur": "Dale Carnegie",
        "Code ISBN": "VGHU",
        "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
        "Editeur": "Haemonies",
        "Titre": "l'art de parler en public",
        "categories_id": 1,
        "id": 12
    },
    "success": true,
    "total": 6
}
# 5 - Enregistrer un livre: Enregistrer un livre en écrivant toutes les références
route: /POST/livres
Résultat:
{
    "created_id": 19
        {
            "Auteur": "Djibril Niane",
            "Code ISBN": "SK",
            "Date de publication": "Tue, 11 Jul 2000 00:00:00 GMT",
            "Editeur": "Présence africaine",
            "Titre": "Soundjata Kéita ou l'épopée Mandingue",
            "categories_id": 7,
            "id": 19
        }

# *GESTION DES CATEGORIES*
# 1- la liste des catégories: 
route: /GET/categories
# Résultat de la requêtes:
"categories": 
        {
            "Categorie": "Ol",
            "id": 1
        },
        {
            "Categorie": "théâtral",
            "id": 6
        },
        {
            "Categorie": "Narratif",
            "id": 7
        }
# 2 - Donner la liste d'une catégorie: permet de resortir les livres d'une catégorie entrée grâce à son id
route:/GET/categories/1/livres
# Résultat de la requête:
"books": 
        {
            "Auteur": "Dale Carnegie",
            "Code ISBN": "VGHU",
            "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
            "Editeur": "Haemonies",
            "Titre": "l'art de parler en public",
            "categories_id": 1,
            "id": 12
        },
        {
            "Auteur": "Dale Carnegie",
            "Code ISBN": "VGHU",
            "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
            "Editeur": "Haemonies",
            "Titre": "l'art de parler en public",
            "categories_id": 1,
            "id": 13
        },
        {
            "Auteur": "Dale Carnegie",
            "Code ISBN": "GODWIN",
            "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
            "Editeur": "Haemonies",
            "Titre": "L' art de parler en public",
            "categories_id": 1,
            "id": 5
        },
        {
            "Auteur": "Boss",
            "Code ISBN": "VGHU",
            "Date de publication": "Sat, 20 Feb 2021 00:00:00 GMT",
            "Editeur": "Jeu",
            "Titre": "L' art de parler en public",
            "categories_id": 1,
            "id": 6
        }
# 3- modifier le libellé d'une catégorie
route: /PATCH/categories/id
# Résultat de la requête:
"success": true,
    "total": 6,
    "updated_category": {
        "Categorie": "Descriptif",
        "id": 1
    },
    "updated_categroie_id": 1

-supprimer une catégorie
route: /DELETE/categories/id
résultat:
"deleted_categorie": {
        "Categorie": "théâtral",
        "id": 6
    },
    "deleted_id": 6,
    "success": true,
    "total remaining": 5

# 4- Enregistrer une nouvelle catégorie
route: /POST/categories
# Résultat de la requête:       
       {
            "Categorie": "Epistolaires",
            "id": 12
        }
    "created_id": 12,
    "success": true,
    "total": 6
# 5 - Chercher une catégorie par son id
route: /GET/categories/id
# Résultat de la requête:
"researched_Id": 12,
    "researched_category": {
        "Categorie": "Epistolaires",
        "id": 12
    },
    "success": true,
    "total": 6

