"""hehe migrate

Revision ID: 248c12b3ccd0
Revises: 
Create Date: 2022-09-21 12:05:29.570195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '248c12b3ccd0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('game', sa.Column('url', sa.String(length=255), nullable=True))
    op.add_column('game', sa.Column('thumbnail', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game', 'thumbnail')
    op.drop_column('game', 'url')
    op.drop_column('game', 'name')
    # ### end Alembic commands ###
