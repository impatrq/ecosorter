from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/medidas")
def medidas():
    while True:
        plas = 5
        vid = 10
        res = 15
        met = 74
        return render_template("medidas.html", plas = plas, vid = vid, res = res, met = met)