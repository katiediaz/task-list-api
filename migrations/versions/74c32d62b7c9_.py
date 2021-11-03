"""empty message

Revision ID: 74c32d62b7c9
Revises: 13358a7981b5
Create Date: 2021-11-03 15:01:52.276092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74c32d62b7c9'
down_revision = '13358a7981b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_complete', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'is_complete')
    # ### end Alembic commands ###