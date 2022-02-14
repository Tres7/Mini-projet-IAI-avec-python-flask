import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import request
from flask import abort
from dotenv import load_dotenv
load_dotenv()

projet = Flask(__name__)
motdepasse='God123'
password=os.getenv('password')
hostname=os.getenv('host')
projet.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:{}@{}:5432/api'.format(password,hostname)
projet.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(projet)

#Déclaration de la classe Livres
###############################################################
class Livres(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(100),nullable=False)
    titre = db.Column(db.String(100),nullable=False)
    date_publication = db.Column(db.DateTime,nullable=True)
    auteur = db.Column(db.String(100),nullable=False)
    editeur = db.Column(db.String(100),nullable=False)
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __init__(self, isbn, titre, date_publication, auteur, editeur, categories_id):
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categories_id = categories_id

    #fonction d'insertion
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # mise à jour
    def update(self):
        db.session.commit()

    # suppression
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Lister tous les livres
    def format(self):
        return {
            'id': self.id,
            'Code ISBN': self.isbn,
            'Titre': self.titre,
            'Date de publication': self.date_publication,
            'Auteur': self.auteur,
            'Editeur': self.editeur,
            'categories_id': self.categories_id
        }

#Déclaration de la classe Categorie
###############################################################
class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key=True)
    libelle_categorie = db.Column(db.String(100),nullable=False)
    thing = db.relationship('Livres', backref='categories',lazy=True)
    def __init__(self,libelle_categorie):
        self.libelle_categorie=libelle_categorie

    # insertion
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # mise à jour
    def update(self):
        db.session.commit()

    # suppression
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'Categorie': self.libelle_categorie
        }

db.create_all()
############CATEGORIE############################
#listes de toutes les catégories
@projet.route('/categories',methods=['GET'])
def get_all_category():
    categories = Categorie.query.all()
    categories_formated = [categorie.format() for categorie in categories]
    return jsonify({
        'success': True,
        'categories': categories_formated,
        'total': len(Categorie.query.all())
    })

#enregistrer une catégorie
@projet.route('/categories',methods=['POST'])
def add_category():
    body = request.get_json()
    new_libelle_categorie = body.get('libelle_categorie', None)
    categorie = Categorie(libelle_categorie=new_libelle_categorie)
    categorie.insert()
    categories = Categorie.query.all()
    categories_formated = [categorie.format() for categorie in categories]
    return jsonify({
        'created_id': categorie.id,
        'success': True,
        'total': len(Categorie.query.all()),
        'Categories': categories_formated
    })

# Modification du libellé d’une categorie
@projet.route('/categories/<int:id>',methods=['PATCH'])
def update_one_category(id):
    categorie = Categorie.query.get(id)
    body = request.get_json()
    categorie.libelle_categorie = body.get('libelle_categorie',None)
    if categorie.libelle_categorie is None:
        abort(400)
    else:
        categorie.update()
        return jsonify({
            'success': True,
            'updated_categroie_id': id,
            'updated_category': categorie.format(),
            'total': Categorie.query.count()
        })

#Chercher une catégorie en particulier par son id
@projet.route('/categories/<int:id>',methods=['GET'])
def research_category(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'researched_Id': id,
            'researched_category': categorie.format(),
            'total': Categorie.query.count()
        })
#lister les livres d'une catégorie
@projet.route('/categories/<int:id>/livres',methods=['GET'])
def get_books_in_a_category(id):
    try:
        livres = Livres.query.filter_by(categories_id=id).all()
        if livres is None:
            abort(404)
        else:
            livres_formated = [livre.format() for livre in livres]
            return jsonify({
                'success':True,
                'books':livres_formated,
                'total': len(livres)
            })
    except:
        abort(400)
#supprimer une categorie
@projet.route('/categories/<int:id>', methods=['DELETE'])
def delete_one_category(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        categorie.delete()
        return jsonify({
            'success': True,
            'deleted_id': id,
            'deleted_categorie': categorie.format(),
            'total remaining': Categorie.query.count()
        })

#capturer la liste des erreurs
@projet.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
    }), 404


@projet.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "----Internal server error----"
    }), 500


@projet.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
    }), 400


###################Requêtes LIVRES##################################
#Listes de tous les livres
@projet.route('/livres',methods=['GET'])
def get_all_books():
    livres = Livres.query.all()
    livres_formated = [livre.format() for livre in livres]
    return jsonify({
        'success': True,
        'livres': livres_formated,
        'total': len(Livres.query.all())
    })

#enregistrer un livre
@projet.route('/livres',methods=['POST'])
def add_book():
    body = request.get_json()
    new_isbn = body.get('isbn',None)
    new_titre = body.get('titre',None)
    new_date_publication = body.get('date_publication',None)
    new_auteur = body.get('auteur',None)
    new_editeur = body.get('editeur',None)
    new_categorie_id = body.get('categorie_id',None)
    livre = Livres(isbn=new_isbn, titre=new_titre, date_publication=new_date_publication, auteur=new_auteur, editeur=new_editeur, categories_id=new_categorie_id)
    livre.insert()
    livres=Livres.query.all()
    livres_formated = [livre.format() for livre in livres]
    return jsonify({
        'created_id': livre.id,
        'success': True,
        'total': len(Livres.query.all()),
        'livres': livres_formated
    })

#Chercher un livre en particulier par son id
@projet.route('/livres/<int:id>',methods=['GET'])
def research_book(id):
    livre = Livres.query.get(id)
    if livre is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'researched_Id': id,
            'researched_book': livre.format(),
            'total': Livres.query.count(),
        })


# supprimer un livre
@projet.route('/livres/<int:id>', methods=['DELETE'])
def delete_one_book(id):
    book = Livres.query.get(id)
    if book is None:
        abort(404)
    else:
        book.delete()
        return jsonify({
            'success': True,
            'deleted_id': id,
            'deleted_book': book.format(),
            'total remaining': Livres.query.count()
        })


#modifier les informations d'un livre
@projet.route('/livres/<int:id>', methods=['PATCH'])
def update_one_book(id):
    book = Livres.query.get(id)
    body = request.get_json()
    book.isbn = body.get('isbn', book.isbn)
    book.titre = body.get('titre', book.titre)
    book.date_publication = body.get('date_publication', book.date_publication)
    book.auteur = body.get('auteur', book.auteur)
    book.editeur = body.get('editeur', book.editeur)
    book.categories_id = body.get('categories_id', book.categories_id)
    if book.isbn is not None or book.titre is not None or book.date_publication is not None or book.auteur is not None or book.editeur is not None or book.categories_id is not None:
        book.update()
        return jsonify({
            'success': True,
            'updated_book_Id': id,
            'new_book': book.format(),
        })

#capturer la liste des erreurs
@projet.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
    }), 404


@projet.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "----Internal server error----"
    }), 500


@projet.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
    }), 400


