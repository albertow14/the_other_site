from jinja2 import Environment, FileSystemLoader, select_autoescape
from flask import Flask, request, jsonify
import pymongo
from scraper.corgis.corgis.pipelines import CorgisPipeline




env = Environment(
    loader=FileSystemLoader('template')

)
title = 'A TITLE'
name = 'KAOS'
elements = ['alberto', 'silvia','gonzalo']
titulo_producto = ['manzana', 'pera', 'piña']

images_interactor = CorgisPipeline()
imagenes = images_interactor.get_all_items()
#urls = [imagen.get('imagenes') for imagen in imagenes]
#print(urls)
productos = [imagen.get('titulo') for imagen in imagenes]




template = env.get_template('index.html')
producto = env.get_template('producto.html')
#my_html = template.render(title=title, name='KAOS', elements=elements, urls=urls[0])
plantilla_producto = producto.render(title=title, name='KAOS', elements=elements, productos=productos[0])




app = Flask(__name__)

def search_for_titles(collection, search_text):
    collection.create_index([('titulo','text')])
    return collection.find({"$text": {"$search": search_text}}).limit(3)

@app.route('/users', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'GET':
        return plantilla_producto
    if request.method == 'POST':
        data = request.json
        word_to_search = data.get('word')
        search = search_for_titles(images_interactor.collection, word_to_search)
        result = list()
        for x in search:
            result.append(x['titulo']) 
        
        return str(result)

@app.route('/blog/<titulo_producto>')
def hello(titulo_producto):
    return plantilla_producto

if __name__ == "__main__":
    app.run() 