from flask import jsonify, Response

from app import app
from .models import ColourVoteCount
from .serializers import colours_vote_count_schema


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return Response('APIs for FavouriteColour')


@app.route('/results', methods=['GET'])
def results():
    colour_vote_count_data = ColourVoteCount.query.all()
    result = colours_vote_count_schema.dump(colour_vote_count_data)
    return jsonify(result.data)
