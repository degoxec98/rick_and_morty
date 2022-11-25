from flask import Blueprint, render_template, redirect, request, flash
from app.models.personaje import Personaje
from app.db import db
from app.requests import Request


rick_y_morty = Blueprint('rick_y_morty', __name__)


@rick_y_morty.route('/', methods=['GET'])
def index():
    personajes=Personaje()

    return render_template('index.html',personajes=personajes)


@rick_y_morty.route('/insertar-personaje', methods = ['GET', 'POST'])
def insertar_personaje():
    personajes = Request().characters()
    print("Personaje 1: ", personajes[0])
    db.personajes.insert_many(personajes)
    # db.personajes.insert_one(personajes[0])
    return 'PERSONAJES INSERTADOS!'
    


@rick_y_morty.route('/perfil')
def profile():
    
    pass