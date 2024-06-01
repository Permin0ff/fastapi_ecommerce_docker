"""create_main_tables

Revision ID: 7e67a9162541
Revises: d7f76dc3dd94
Create Date: 2024-05-30 08:19:37.095016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e67a9162541'
down_revision: Union[str, None] = 'd7f76dc3dd94'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
