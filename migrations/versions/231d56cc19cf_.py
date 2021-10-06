"""empty message

Revision ID: 231d56cc19cf
Revises: 
Create Date: 2021-09-14 22:42:26.864639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '231d56cc19cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offices',
    sa.Column('usa_state', sa.String(length=10), nullable=True),
    sa.Column('office_code', sa.String(length=10), nullable=False),
    sa.Column('office_name', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('office_code')
    )
    op.create_table('orders',
    sa.Column('order_number', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=40), nullable=False),
    sa.Column('usa_state', sa.String(length=10), nullable=True),
    sa.Column('office_code', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['office_code'], ['offices.office_code'], ),
    sa.PrimaryKeyConstraint('order_number')
    )
    op.create_index(op.f('ix_orders_uuid'), 'orders', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_uuid'), table_name='orders')
    op.drop_table('orders')
    op.drop_table('offices')
    # ### end Alembic commands ###