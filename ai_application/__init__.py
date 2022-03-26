from flask import Flask
import os

app = Flask(__name__)
app.config['RECOGNIZER_MODEL'] = os.getenv('RECOGNIZER_MODEL')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')

import ai_application.views