"""changes to user and worker

Revision ID: 0359b9cb2818
Revises: f8b97e26ff30
Create Date: 2024-06-17 18:43:06.555897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0359b9cb2818'
down_revision: Union[str, None] = 'f8b97e26ff30'
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