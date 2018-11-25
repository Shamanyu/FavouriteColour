"""empty message

Revision ID: e1d5b8b28be7
Revises: 
Create Date: 2018-11-25 21:28:19.981288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1d5b8b28be7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('colour_vote_count',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('colour', sa.String(length=10), nullable=False),
    sa.Column('colour_code', sa.String(length=7), nullable=False),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('colour'),
    sa.UniqueConstraint('colour_code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('colour_vote_count')
    # ### end Alembic commands ###