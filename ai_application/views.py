from flask import render_template, request, flash, redirect
from ai_application import app
from werkzeug.utils import secure_filename
import os
import base64
from ai_application.recognizer import recognize

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_base64_image(full_path):
    encoded_string = None
    with open(full_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/recognize', methods=('GET', 'POST'))
def recognize():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            full_path = None
            base64_image = None
            try:
                filename = secure_filename(file.filename)
                full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(full_path)
                base64_image = get_base64_image(full_path)
            finally:
                if full_path != None:
                    os.remove(full_path)
            return render_template("recognize.html", prediction=None, base64_image=base64_image)

    return render_template("recognize.html", prediction=None, base64_image=None)
