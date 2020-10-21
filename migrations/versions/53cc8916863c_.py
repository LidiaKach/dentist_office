"""empty message

Revision ID: 53cc8916863c
Revises: 80379ec79afe
Create Date: 2020-10-21 15:47:02.017358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53cc8916863c'
down_revision = '80379ec79afe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('city', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'city')
    # ### end Alembic commands ###
