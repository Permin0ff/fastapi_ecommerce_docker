"""create_main_tables

Revision ID: 42ebf0531b3a
Revises: 7e67a9162541
Create Date: 2024-05-30 08:20:27.916870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42ebf0531b3a'
down_revision: Union[str, None] = '7e67a9162541'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
