from flask import Flask
import os, requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))