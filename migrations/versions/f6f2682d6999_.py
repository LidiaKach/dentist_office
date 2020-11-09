"""empty message

Revision ID: f6f2682d6999
Revises: 3644ad4a70be
Create Date: 2020-10-22 15:36:22.500259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6f2682d6999'
down_revision = '3644ad4a70be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('patients', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('patients', 'street',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('patients', 'street',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('patients', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###
