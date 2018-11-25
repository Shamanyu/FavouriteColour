from app import db

class ColourVoteCount(db.Model):
    colour = db.Column(db.String(10), index=True, unique=True)
    votes = db.Column(db.String(120))

    def __repr__(self):
        return '<ColourVoteCount- Color:{} Votes:{}>'.format(self.colour, self.votes)