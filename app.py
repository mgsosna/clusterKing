import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify

from static.python import DataGenerator
dg = DataGenerator()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data_rings")
def data_rings():
    return jsonify(dg.create_rings())

@app.route("/data_moons")
def data_moons():
    return jsonify(dg.create_moons())


if __name__ == "__main__":
    app.run(debug=True)
