from flask import render_template, request
from ai_application import app

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/recognize', methods=('GET', 'POST'))
def recognize():
    if request.method == 'POST':
        pass
    return render_template("recognize.html", prediction=None, base64_image=None)
