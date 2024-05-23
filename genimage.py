from flask import Blueprint, render_template, request, url_for, redirect
import base64
from db import DATABASE_URL
from controller import *

genimage = Blueprint("genimage", __name__)

@genimage.route("/generate/image")
def generate_image():
    return render_template("generate.html", title="Generate Image")

@genimage.route("/generate/image/store", methods=['POST'])
def generate_image_store():
    prompt = request.form.get('prompt')
    image = request.files['image']
    
    store_image(DATABASE_URL, prompt, image.read())
    
    return 'Image stored successfully'

@genimage.route("/generate/image/history")
def generate_image_history():
    history_data = get(DATABASE_URL)
    processed_history_data = []
    for row in history_data:
        row_list = list(row)
        row_list[2] = base64.b64encode(row[2]).decode('utf-8')
        processed_history_data.append(row_list)
        processed_history_data = sorted(processed_history_data, key=lambda x: x[0], reverse=True)
    return render_template("imagehistory.html", title="History Image Generation", history_data=processed_history_data)

@genimage.route("/generate/image/history/reset")
def generate_image_history_reset():
    reset(DATABASE_URL)
    return redirect(url_for('generate_image_history'))