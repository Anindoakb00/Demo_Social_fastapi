"""add last few column to post table

Revision ID: 630df249b905
Revises: dd871aa4f595
Create Date: 2024-10-27 14:33:39.874507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '630df249b905'
down_revision: Union[str, None] = 'dd871aa4f595'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('post', sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='TRUE' ),)
    op.add_column('post',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')
    ),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
  