from app import ma


class ColourVoteCountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'colour', 'colour_code', 'votes')


colour_vote_count_schema = ColourVoteCountSchema()
colours_vote_count_schema = ColourVoteCountSchema(many=True)