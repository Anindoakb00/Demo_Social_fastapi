"""create post table

Revision ID: 2318240cdcd8
Revises: 
Create Date: 2024-10-21 18:04:27.440543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2318240cdcd8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('post',sa.Column('id',sa.Integer(), nullable=False,primary_key=True)
    ,sa.Column('title',sa.String(),nullable=False))
   



def downgrade():
    op.drop_table('posts')
    
