from flask import render_template
from ai_application import app

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/recognize', methods=('GET', 'POST'))
def recognize():
    return render_template("recognize.html")
