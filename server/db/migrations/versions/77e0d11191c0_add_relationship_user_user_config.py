"""add relationship user-user_config

Revision ID: 77e0d11191c0
Revises: 3d34fa51a7be
Create Date: 2023-10-28 21:47:57.197586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77e0d11191c0'
down_revision: Union[str, None] = '3d34fa51a7be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
