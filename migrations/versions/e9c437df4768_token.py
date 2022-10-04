"""token

Revision ID: e9c437df4768
Revises: 248c12b3ccd0
Create Date: 2022-10-04 17:29:18.818007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9c437df4768'
down_revision = '248c12b3ccd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('token', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('token', sa.Column('code', sa.String(length=6), nullable=True))
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('token', 'code')
    op.drop_column('token', 'email')
    # ### end Alembic commands ###
