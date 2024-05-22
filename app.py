from flask import Flask, render_template, redirect, url_for, jsonify, request
import os, base64
from db import DATABASE_URL, DATABASE_URL_2
from controller import *
from operator import itemgetter

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

@app.route("/generate/image/store", methods=['POST'])
def generate_image_store():
    prompt = request.form.get('prompt')
    image = request.files['image']
    
    store_image(DATABASE_URL, prompt, image.read())
    
    return 'Image stored successfully'

@app.route("/generate/image/history")
def generate_image_history():
    history_data = get(DATABASE_URL)
    processed_history_data = []
    for row in history_data:
        row_list = list(row)
        row_list[2] = base64.b64encode(row[2]).decode('utf-8')
        processed_history_data.append(row_list)
        processed_history_data = sorted(processed_history_data, key=lambda x: x[0], reverse=True)
    return render_template("imagehistory.html", title="History Image Generation", history_data=processed_history_data)

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
    history_data.sort(key=itemgetter(0), reverse=True)
    return render_template("texthistory.html", title="History Text Generation", history_data=history_data)

@app.route("/generate/text/store", methods=['GET'])
def generate_text_store():
    prompt = request.args.get('prompt')
    text = request.args.get('text')
    store_text(DATABASE_URL_2, prompt, text)

    return jsonify({'status': 'success', 'prompt': prompt, 'text': text})

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