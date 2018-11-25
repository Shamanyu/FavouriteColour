from app import app
from .models import ColourVoteCount

@app.route('/results', methods=['GET'])
def results():
    a = ColourVoteCount.query.get(ident=1)
    print (a)