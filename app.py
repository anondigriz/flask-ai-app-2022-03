from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/recognize', methods=('GET', 'POST'))
def recognize():
    return render_template("recognize.html")
