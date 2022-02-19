"""empty message

Revision ID: c9a8bf891bec
Revises: 
Create Date: 2022-02-19 18:27:50.486516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9a8bf891bec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('account_number', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_number')
    )
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_number_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('transaction_details', sa.String(), nullable=True),
    sa.Column('value_date', sa.String(), nullable=True),
    sa.Column('withdraw_amount', sa.String(), nullable=True),
    sa.Column('deposit_amount', sa.String(), nullable=True),
    sa.Column('balance_amount', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['account_number_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    op.drop_table('users')
    # ### end Alembic commands ###
