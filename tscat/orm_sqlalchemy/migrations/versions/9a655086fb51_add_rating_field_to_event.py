"""add rating field to event

Revision ID: 9a655086fb51
Revises: 0c057a8951ba
Create Date: 2024-03-18 19:04:13.369691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a655086fb51'
down_revision: Union[str, None] = '0c057a8951ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('events', sa.Column('rating', sa.Integer(), nullable=True))


def downgrade() -> None:
    raise NotImplementedError("Downgrade is not supported.")
