"""create_main_tables

Revision ID: 8813e036d1e1
Revises: 42ebf0531b3a
Create Date: 2024-05-30 08:21:25.141562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8813e036d1e1'
down_revision: Union[str, None] = '42ebf0531b3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
