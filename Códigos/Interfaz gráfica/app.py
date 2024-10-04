from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/medidas")
def medidas():
    while True:
        plas = 10
        vid = 10
        res = 15
        met = 10
        detPlas = 0
        detMet = 0
        detRes = 1
        detVid = 0
        return render_template("medidas.html", 
                               plas = plas,
                               vid = vid,
                               res = res,
                               met = met,
                               detPlas = detPlas,
                               detMet = detMet,
                               detRes = detRes,
                               detVid = detVid)