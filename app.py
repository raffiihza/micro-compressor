from flask import Flask, render_template, redirect, url_for
import os, requests

app = Flask(__name__)

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

@app.route("/generate/text")
def generate_text():
    return render_template("llm.html", title="Generate Text")

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