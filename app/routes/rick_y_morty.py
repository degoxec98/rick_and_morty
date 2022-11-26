from flask import Blueprint, render_template, redirect, request, flash, url_for
from app.models.personaje import Personaje
from app.db import db
from app.requests import Request


rick_y_morty = Blueprint('rick_y_morty', __name__)


@rick_y_morty.route('/', methods=['GET'])
def index():
    personajes = db.personajes.find()
    return render_template('index.html',personajes=personajes)


@rick_y_morty.route('/insertar-personaje', methods = ['GET', 'POST'])
def insertar_personaje():
    personajes = Request().characters()
    db.personajes.insert_many(personajes)
    return 'PERSONAJES INSERTADOS!'


@rick_y_morty.route('/profile', defaults = {'id': None})
@rick_y_morty.route('/profile/', defaults = {'id': None})
@rick_y_morty.route('/profile/<int:id>')
def profile(id = None):
    if id == None:
        return redirect('/')
    personaje = db.personajes.find_one({'id':int(id)})
    if personaje == None:
        return redirect('/')
    
    return render_template("profile.html", personaje = personaje)
    