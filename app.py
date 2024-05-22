from flask import Flask, render_template, redirect, url_for, jsonify
import os
from db import DATABASE_URL, DATABASE_URL_2
from controller import *

app = Flask(__name__)
    
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

@app.route("/generate/image")
def generate_image():
    return render_template("generate.html", title="Generate Image")

@app.route("/generate/image/history")
def generate_image_history():
    history_data = get(DATABASE_URL)
    return render_template("imagehistory.html", title="History Image Generation", history_data=history_data)

@app.route("/generate/image/history/reset")
def generate_image_history_reset():
    reset(DATABASE_URL)
    return redirect(url_for('generate_image_history'))

@app.route("/generate/text")
def generate_text():
    return render_template("llm.html", title="Generate Text")

@app.route("/generate/text/history")
def generate_text_history():
    history_data = get(DATABASE_URL_2)
    return render_template("texthistory.html", title="History Text Generation", history_data=history_data)

@app.route("/generate/text/store")
def generate_text_store():
    return 'test'

@app.route("/generate/text/history/reset")
def generate_text_history_reset():
    reset(DATABASE_URL_2)
    return redirect(url_for('generate_text_history'))

@app.route("/search/weather")
def search_weather():
    return render_template("weather.html", title="Search Weather")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))