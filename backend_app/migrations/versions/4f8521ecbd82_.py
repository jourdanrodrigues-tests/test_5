"""empty message
Revision ID: 4f8521ecbd82
Revises:
Create Date: 2018-05-13 21:28:33.969129
"""
import sqlalchemy as sa
from alembic import op

revision = '4f8521ecbd82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comment',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('time', sa.Integer(), nullable=False),
        sa.Column('dead', sa.Boolean(), nullable=False),
        sa.Column('deleted', sa.Boolean(), nullable=False),
        sa.Column('parent_id', sa.Integer(), nullable=False),
        sa.Column('author', sa.String(length=20), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'story',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('time', sa.Integer(), nullable=False),
        sa.Column('points', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(length=200), nullable=True),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('author', sa.String(length=20), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('title'),
    )


def downgrade():
    op.drop_table('story')
    op.drop_table('comment')
