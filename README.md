# Image Scraper

Una herramienta web simple para extraer y descargar imágenes de cualquier página web. Desarrollada con Python y Flask.

## Características

- Extrae todas las imágenes de una URL proporcionada
- Muestra las imágenes en una cuadrícula responsive
- Permite seleccionar múltiples imágenes mediante checkboxes
- Descarga las imágenes seleccionadas en un archivo ZIP
- Proporciona enlaces directos a las imágenes originales
- Muestra información adicional de cada imagen (alt text, título)
- Convierte URLs relativas a absolutas automáticamente
- Interfaz intuitiva y fácil de usar


## Instalación (GitHub Codespaces)

1. Abre el proyecto en GitHub Codespaces

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
## Uso

1. Ejecuta la aplicación: 

```bash
python app.py
```

2. Abre la URL proporcionada por Codespaces

3. Introduce la URL de la página web de la que quieres extraer las imágenes

4. Haz clic en "Extraer Imágenes"

5. Selecciona las imágenes que deseas descargar usando los checkboxes

6. Haz clic en "Descargar Seleccionadas" para obtener un archivo ZIP con las imágenes

## Tecnologías utilizadas

- Python
- Flask
- BeautifulSoup4
- Requests
- HTML/CSS
- JavaScript
- ZIP file handling

## Requisitos
Ver requirements.txt para las versiones específicas:

- Flask==2.2.5
- Werkzeug==2.2.3
- requests==2.31.0
- beautifulsoup4==4.12.2

## Contribuir

Las contribuciones son bienvenidas. Siéntete libre de abrir issues o pull requests para mejorar este proyecto.

## Contacto

Para cualquier consulta o colaboración, puedes contactar al autor a través de:

- GitHub: [EduardoHernandezGuzman](https://github.com/EduardoHernandezGuzman)