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
rolling_stones = Base.classes.rolling_stones
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

#Rolling Stones Data
@app.route("/rollingdata")
def rollingdata():

    sel = [
        rolling_stones.Number,
        rolling_stones.Year,
        rolling_stones.Album,
        rolling_stones.Artist,
        rolling_stones.Genre
    ]

    results1 = db.session.query(*sel).all()

    rolling_data = []
    for result in results1:
        rolling_data.append({
            "Number": result[0],
            "Year": result[1],
            "Album": result[2],
            "Artist": result[3],
            "Genre": result[4]
        })
    print(rolling_data)
    return jsonify(rolling_data)

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
            "genre_count": result[1],
            "genre": result[2],
            "avg score": result[3],
            "year": result[4]
        })
    return jsonify(pitch_total_data)

@app.route("/pitchfork/<album_title>")
def pitchfork_data(album_title):

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
    results = db.session.query(*sel).filter(PitchforkData.album_title == album_title).all()

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

@app.route("/1999")
def ninetynine():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 1999).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2000")
def zero():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2000).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2001")
def one():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2001).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)


@app.route("/2002")
def two():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2002).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2003")
def three():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2003).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2004")
def four():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2004).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2005")
def five():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2005).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2006")
def six():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2006).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2007")
def seven():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2007).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2008")
def eight():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2008).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2009")
def nine():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2009).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2010")
def ten():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2010).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2011")
def eleven():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2011).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
    return jsonify(pitch_data)

@app.route("/2012")
def twelve():
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

    results1 = db.session.query(*sel).filter(PitchforkData.year == 2012).all()

    pitch_data = []
    for result in results1:
        pitch_data.append({
        "reviewid": result[0],
        "artist": result[1],
        "genre": result[2],
        "album_title": result[3],
        "score": result[4],
        "pub_year": result[5],
        "year": result[6],
        "url": result[7]
        })
    
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