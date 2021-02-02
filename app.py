import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify, redirect, request

from static.python import DataGenerator, ClusterLabeler
dg = DataGenerator()
cl = ClusterLabeler()

app = Flask(__name__)

@app.route("/blobs")
@app.route("/")
def blobs():
    return render_template("blobs.html")


@app.route("/moons")
def moons():
    return render_template("moons.html")


@app.route("/rings")
def rings():
    return render_template("rings.html")


@app.route("/uniform")
def uniform():
    return render_template("uniform.html")


@app.route("/data/<string:dtype>", methods=['POST'])
def data(dtype):

    input_dict = request.get_json()

    # Convert all keys to float
    for key in input_dict.keys():
        input_dict[key] = float(input_dict[key])

    if dtype == 'blobs':
        return jsonify('')
        # return jsonify(dg.create_blobs(**input_dict))
    elif dtype == 'moons':
        return jsonify(dg.create_moons(**input_dict))
    elif dtype == 'rings':
        return jsonify(dg.create_rings(**input_dict))
    elif dtype == 'uniform':
        return jsonify('')
        # return jsonify(dg.create_uniform(**input_dict))
    else:
        return jsonify(f"Error: {dtype} endpoint does not exist"), 404


@app.route("/cluster/<string:algo>", methods=['POST'])
def cluster(algo):

    input_dict = request.get_json()

    # Convert all values to floats
    for key in input_dict.keys():
        input_dict[key] = [float(val) for val in input_dict[key]]

    if algo == 'kmeans':
        return jsonify(cl.kmeans(input_dict))

if __name__ == "__main__":
    app.run(debug=True)
