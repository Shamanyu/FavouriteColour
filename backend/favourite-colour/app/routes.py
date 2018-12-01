from flask import jsonify, Response
from flask_cors import CORS, cross_origin
from flask import request
import json

from app import app
from app import db
from .models import ColourVoteCount
from .serializers import colours_vote_count_schema


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def index():
    return Response('APIs for FavouriteColour')


@app.route('/results', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def results():
    colour_vote_count_data = ColourVoteCount.query.all()
    result = colours_vote_count_schema.dump(colour_vote_count_data)
    return jsonify(result.data)


@app.route('/vote', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def vote():
    try:
        data = json.loads(request.data)
        colour = data['colour']
        colour_object = ColourVoteCount.query.filter_by(colour=colour).first()
        colour_object.votes += 1
        db.session.add(colour_object)
        db.session.commit()
        return Response('Thank you! Your vote has been taken into account.')
    except:
        return Response('Bad data. Vote ignored.')

