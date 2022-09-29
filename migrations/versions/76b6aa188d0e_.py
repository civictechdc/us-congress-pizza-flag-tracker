"""empty message

Revision ID: 76b6aa188d0e
Revises: 0cf6986c9068
Create Date: 2022-09-28 19:30:02.557525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76b6aa188d0e'
down_revision = '0cf6986c9068'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_logs', sa.Column('order_archived', sa.Integer(), nullable=True))
    op.add_column('orders', sa.Column('archived', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'archived')
    op.drop_column('order_logs', 'order_archived')
    # ### end Alembic commands ###