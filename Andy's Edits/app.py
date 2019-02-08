#Dependencies
import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/database.sqlite"
db = SQLAlchemy(app)

#Database Model
Base = automap_base()
Base.prepare(db.engine, reflect=True)
Base.classes.keys()

#Reference for each data tables in sqlite
PitchforkData = Base.classes.cleanup_list
totals_pitchfork = Base.classes.cleanup_list_totals

#Trying to resolve an error
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

#Home page
@app.route("/")
def index():

    return render_template("index.html")

@app.route('/<page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route("/visualization-1-col")
def visual1():

    return render_template("visualization-1-col.html")

#Pitch Data
@app.route("/pitchdata")
def pitchdata():
    #Defining our selection for the query
    sel = [
        PitchforkData.reviewid,
        PitchforkData.artist,
        PitchforkData.genre,
        PitchforkData.album_title,
        PitchforkData.score,
        PitchforkData.pub_year,
        PitchforkData.year,
        PitchforkData.url
        ]
    
    results1 = db.session.query(*sel).all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "reviewid": result[0],
            "artist": result[1],
            "genre": result[2],
            "album_title": result[3],
            "score": result[4],
            "pub_year": result[5],
            "year": result[6],
            "url": result[7]
        })
    print(results1)
    return jsonify(pitch_data1)

@app.route("/pitchtotals")
def pitchtotals():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year
    ]

    results2 = db.session.query(*sel).all()

    pitch_total_data = []
    for result in results2:
        pitch_total_data.append({
            "id": result[0],
            "genre count": result[1],
            "genre": result[2],
            "avg score": result[3],
            "year": result[4]
        })
    return jsonify(pitch_total_data)

@app.route("/pitchfork/<reviewid>")
def pitchfork_data(reviewid):

    #Defining our selection for the query
    sel = [
        PitchforkData.reviewid,
        PitchforkData.artist,
        PitchforkData.genre,
        PitchforkData.album_title,
        PitchforkData.score,
        PitchforkData.pub_year,
        PitchforkData.year,
        PitchforkData.url
        ]
    
    #Run the query and store it in results
    results = db.session.query(*sel).filter(PitchforkData.reviewid == reviewid).all()

    #dictionary for the query data
    pitch_data = {}
    for result in results:
        pitch_data["reviewid"] = result[0]
        pitch_data["artist"] = result[1]
        pitch_data["genre"] = result[2]
        pitch_data["album_title"] = result[3]
        pitch_data["score"] = result[4]
        pitch_data["pub_year"] = result[5]
        pitch_data["year"] = result[6]
        pitch_data["url"] = result[7]
    
    # print(pitch_data)
    return jsonify(pitch_data)

@app.route("/rock")
def rock():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year,
        ]

    results1 = db.session.query(*sel).filter(totals_pitchfork.genre == "rock").all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "id": result[0],
            "genre_count": result[1],
            "genre": result[2],
            "avg_score": result[3],
            "year": result[4]
        })
    # print(pitch_data1)
    return jsonify(pitch_data1)

@app.route("/global")
def global1():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year,
        ]

    results1 = db.session.query(*sel).filter(totals_pitchfork.genre == "global").all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "id": result[0],
            "genre_count": result[1],
            "genre": result[2],
            "avg_score": result[3],
            "year": result[4]
        })
    # print(pitch_data1)
    return jsonify(pitch_data1)

@app.route("/rap")
def rap():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year,
        ]

    results1 = db.session.query(*sel).filter(totals_pitchfork.genre == "rap").all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "id": result[0],
            "genre_count": result[1],
            "genre": result[2],
            "avg_score": result[3],
            "year": result[4]
        })
    # print(pitch_data1)
    return jsonify(pitch_data1)

@app.route("/pop/r&b")
def pop_rb():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year,
        ]

    results1 = db.session.query(*sel).filter(totals_pitchfork.genre == "pop/r&b").all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "id": result[0],
            "genre_count": result[1],
            "genre": result[2],
            "avg_score": result[3],
            "year": result[4]
        })
    # print(pitch_data1)
    return jsonify(pitch_data1)

@app.route("/metal")
def metal():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year,
        ]

    results1 = db.session.query(*sel).filter(totals_pitchfork.genre == "metal").all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "id": result[0],
            "genre_count": result[1],
            "genre": result[2],
            "avg_score": result[3],
            "year": result[4]
        })
    # print(pitch_data1)
    return jsonify(pitch_data1)

@app.route("/jazz")
def jazz():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year,
        ]

    results1 = db.session.query(*sel).filter(totals_pitchfork.genre == "jazz").all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "id": result[0],
            "genre_count": result[1],
            "genre": result[2],
            "avg_score": result[3],
            "year": result[4]
        })
    # print(pitch_data1)
    return jsonify(pitch_data1)

@app.route("/folk/country")
def folk_country():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year,
        ]

    results1 = db.session.query(*sel).filter(totals_pitchfork.genre == "folk/country").all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "id": result[0],
            "genre_count": result[1],
            "genre": result[2],
            "avg_score": result[3],
            "year": result[4]
        })
    # print(pitch_data1)
    return jsonify(pitch_data1)

@app.route("/electronic")
def electronic():
    sel = [
        totals_pitchfork.id,
        totals_pitchfork.genre_count,
        totals_pitchfork.genre,
        totals_pitchfork.avg_score,
        totals_pitchfork.year,
        ]

    results1 = db.session.query(*sel).filter(totals_pitchfork.genre == "electronic").all()

    pitch_data1 = []
    for result in results1:
        pitch_data1.append({
            "id": result[0],
            "genre_count": result[1],
            "genre": result[2],
            "avg_score": result[3],
            "year": result[4]
        })
    # print(pitch_data1)
    return jsonify(pitch_data1)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
# app.run()