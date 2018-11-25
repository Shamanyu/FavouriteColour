from flask import Response, jsonify

from app import app
from .models import ColourVoteCount

@app.route('/results', methods=['GET'])
def results():
    colour_vote_count_object = ColourVoteCount.query.filter_by(colour='red').first()
    return jsonify({
            'colour': colour_vote_count_object.colour,
            'votes': colour_vote_count_object.votes
        })
