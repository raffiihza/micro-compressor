from flask import Flask, request, send_file, after_this_request
from werkzeug.utils import secure_filename
from pypdf import PdfReader, PdfWriter
from flask_cors import CORS
import os
import uuid

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/', methods=['GET', 'HEAD'])
def health_check():
    return "The service is up"

@app.route('/compress', methods=['POST'])
def compress_pdf():
    file = request.files['file']
    unique_filename = str(uuid.uuid4())
    filename = f'{unique_filename}.pdf'
    file_path = os.path.join(os.getcwd(), filename)
    file.save(file_path)

    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=60)

    writer.add_metadata(reader.metadata)

    out_filename = "out_" + filename
    out_file_path = os.path.join(os.getcwd(), out_filename)
    with open(out_file_path, "wb") as f:
        writer.write(f)

    # Delete the original file after processing
    os.remove(file_path)

    @after_this_request
    def remove_file(response):
        try:
            os.remove(out_file_path)
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response

    return send_file(out_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
