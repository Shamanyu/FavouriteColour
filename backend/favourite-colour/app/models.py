from app import db


class ColourVoteCount(db.Model):
    __tablename__ = 'colour_vote_count'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    colour = db.Column(db.String(10), unique=True, nullable=False)
    colour_code = db.Column(db.String(7), unique=True, nullable=False)
    votes = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<ColourVoteCount- Color:{} Votes:{}>'.format(self.colour, self.votes)