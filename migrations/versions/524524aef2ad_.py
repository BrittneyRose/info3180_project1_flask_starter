"""empty message

Revision ID: 524524aef2ad
Revises: 
Create Date: 2024-03-13 00:10:03.004977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '524524aef2ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('room_num', sa.String(length=80), nullable=True),
    sa.Column('bathroom_num', sa.String(length=80), nullable=True),
    sa.Column('price', sa.String(length=80), nullable=True),
    sa.Column('property_type', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('photo_filename', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property_profiles')
    # ### end Alembic commands ###
