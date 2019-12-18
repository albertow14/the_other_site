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
urls = [imagen.get('imagenes') for imagen in imagenes]
print(urls)

template = env.get_template('index.html')
producto = env.get_template('producto.html')
my_html = template.render(title=title, name='KAOS', elements=elements, urls=urls[0])
plantilla_producto = producto.render(title=title, name='KAOS', elements=elements, titulo_producto=titulo_producto)




app = Flask(__name__)

@app.route('/users', methods=['GET'])
def hello_world():

    if request.method == 'GET':
        return my_html

@app.route('/blog/<titulo_producto>')
def hello(titulo_producto):
    return plantilla_producto

if __name__ == "__main__":
    app.run() 