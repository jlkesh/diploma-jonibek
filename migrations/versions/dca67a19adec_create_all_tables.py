"""Create all tables

Revision ID: dca67a19adec
Revises: 
Create Date: 2022-04-13 13:12:43.776836

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dca67a19adec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("test",
                    sa.Column('id', sa.Integer(), primary_key=True),
                    sa.Column('field_name', sa.String(100), nullable=False))


def downgrade():
    op.drop_table("test")
