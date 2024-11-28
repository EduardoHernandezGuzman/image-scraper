import io
import zipfile
from flask import Flask, render_template, request, jsonify, send_file
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
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        images = []
        for img in soup.find_all('img'):
            img_url = img.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                
                alt_text = img.get('alt', '')
                title = img.get('title', '')
                
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

@app.route('/download', methods=['POST'])
def download():
    try:
        urls = request.json.get('urls', [])
        
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zf:
            for i, url in enumerate(urls):
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    
                    ext = url.split('.')[-1].split('?')[0]
                    if ext.lower() not in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']:
                        ext = 'jpg'
                    
                    zf.writestr(f'image_{i+1}.{ext}', response.content)
                except Exception as e:
                    print(f"Error downloading {url}: {str(e)}")
                    continue
        
        memory_file.seek(0)
        
        return send_file(
            memory_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name='images.zip'
        )
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)