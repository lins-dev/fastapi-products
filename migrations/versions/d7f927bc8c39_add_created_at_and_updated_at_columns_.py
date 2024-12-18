"""add_created_at_and_updated_at_columns_in_categories_table

Revision ID: d7f927bc8c39
Revises: c4c9e5050411
Create Date: 2024-11-27 21:30:09.794352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7f927bc8c39'
down_revision: Union[str, None] = 'c4c9e5050411'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('categories', sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('categories', 'updated_at')
    op.drop_column('categories', 'created_at')
    # ### end Alembic commands ###
