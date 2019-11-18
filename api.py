
from flask import Flask
import json

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "/home/otavio/PycharmProjects/untitled"

@app.route("/resposta", methods=['GET','POST'])
def index():
    return json.load(open("dados.json"))