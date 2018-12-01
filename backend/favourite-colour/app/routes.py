from flask import jsonify

from app import app
from .models import ColourVoteCount
from .serializers import colours_vote_count_schema


@app.route('/results', methods=['GET'])
def results():
    colour_vote_count_data = ColourVoteCount.query.all()
    result = colours_vote_count_schema.dump(colour_vote_count_data)
    return jsonify(result.data)
