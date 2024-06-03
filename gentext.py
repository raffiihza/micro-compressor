from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from operator import itemgetter
from db import DATABASE_URL_2
from controller import *

gentext = Blueprint("gentext", __name__)

@gentext.route("/generate/text")
def generate_text():
    return render_template("llm.html", title="Generate Text")

@gentext.route("/generate/text/history")
def generate_text_history():
    history_data = get(DATABASE_URL_2)
    history_data.sort(key=itemgetter(0), reverse=True)
    return render_template("texthistory.html", title="History Text Generation", history_data=history_data)

@gentext.route("/generate/text/store", methods=['GET'])
def generate_text_store():
    prompt = request.args.get('prompt')
    text = request.args.get('text')
    store_text(DATABASE_URL_2, prompt, text)

    return jsonify({'status': 'success', 'prompt': prompt, 'text': text})

@gentext.route("/generate/text/history/reset")
def generate_text_history_reset():
    reset(DATABASE_URL_2)
    return redirect(url_for('gentext.generate_text_history'))