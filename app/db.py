from pymongo import MongoClient

cliente = MongoClient('localhost', 27017) #,usernameroot , aunque yp no tengo

# db=cliente['libros_flask'] #db name
db=cliente['rickymorty']
