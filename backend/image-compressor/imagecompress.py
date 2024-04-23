from flask import Flask, request, send_file, after_this_request
from flask_cors import CORS
from PIL import Image, ImageOps
import io
import os
import uuid

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/compress', methods=['POST'])
def compress_image():
    file = request.files['image']
    image = Image.open(file.stream)
    
    # Adjust image orientation based on EXIF data
    image = ImageOps.exif_transpose(image)
    
    # Generate a unique filename
    unique_filename = str(uuid.uuid4())
    
    # Compress image
    if file.filename.lower().endswith('.jpg') or file.filename.lower().endswith('.jpeg'):
        image.save(f'{unique_filename}.jpg', 'JPEG', quality=60)
        filepath = f'{unique_filename}.jpg'
        mimetype = 'image/jpeg'
    elif file.filename.lower().endswith('.png'):
        image.save(f'{unique_filename}.png', 'PNG', compress_level=5, optimize=True, quality=85)
        filepath = f'{unique_filename}.png'
        mimetype = 'image/png'
    else:
        return "Unsupported image format", 400

    @after_this_request
    def delete_file(response):
        try:
            os.remove(filepath)
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response

    return send_file(filepath, mimetype=mimetype)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
