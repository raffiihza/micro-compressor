from flask import Flask, render_template, redirect, url_for
import os
from controller import *
from genimage import genimage
from gentext import gentext

app = Flask(__name__)
    
# Import blueprints
app.register_blueprint(genimage)
app.register_blueprint(gentext)

# Routes
@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/compress/image")
def compress_image():
    return render_template("imagecompress.html", title="Compress Image")

@app.route("/compress/pdf")
def compress_pdf():
    return render_template("pdfcompress.html", title="Compress PDF")

@app.route("/search/weather")
def search_weather():
    return render_template("weather.html", title="Search Weather")

@app.route("/transcribe")
def transcribe():
    return render_template("transcribe.html", title="Transcribe Sound to Text")

@app.route("/chat/pdf")
def chat_pdf():
    return render_template("chatpdf.html", title="PDF Communicator AI")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))