"""add content column to posts table

Revision ID: 99b7624e49b7
Revises: 2318240cdcd8
Create Date: 2024-10-27 10:27:27.053706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99b7624e49b7'
down_revision: Union[str, None] = '2318240cdcd8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('post', sa.Column('content', sa.String(), nullable=False))
    


def downgrade():
    op.drop_column('post','content')
   
