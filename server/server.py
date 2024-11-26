from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route("/classify")
def classify_img():
    img_data = request.form['img_data']