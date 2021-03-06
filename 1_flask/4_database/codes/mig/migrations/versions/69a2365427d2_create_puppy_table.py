"""create puppy table

Revision ID: 69a2365427d2
Revises: 
Create Date: 2021-05-19 13:37:00.024166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69a2365427d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
