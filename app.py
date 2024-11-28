from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

app = Flask(__name__)

def is_valid_url(url):
    """Verifica si una URL es válida"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def extract_images(url):
    """Extrae todas las imágenes de una URL dada"""
    try:
        # Realizar la petición HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        
        # Parsear el HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar todas las etiquetas de imagen
        images = []
        for img in soup.find_all('img'):
            img_url = img.get('src')
            if img_url:
                # Convertir URLs relativas a absolutas
                img_url = urljoin(url, img_url)
                
                # Obtener información adicional
                alt_text = img.get('alt', '')
                title = img.get('title', '')
                
                # Añadir a la lista solo si es una URL válida
                if is_valid_url(img_url):
                    images.append({
                        'url': img_url,
                        'alt': alt_text,
                        'title': title
                    })
        
        return {
            'success': True,
            'images': images,
            'count': len(images)
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    url = request.json.get('url', '')
    
    if not is_valid_url(url):
        return jsonify({
            'success': False,
            'error': 'URL inválida'
        })
    
    result = extract_images(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)