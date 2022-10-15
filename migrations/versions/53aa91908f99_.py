"""empty message

Revision ID: 53aa91908f99
Revises: 055fd238f994
Create Date: 2022-10-14 18:54:49.024329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53aa91908f99'
down_revision = '055fd238f994'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('salt', sa.String(length=200), nullable=False))
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=200),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
    op.drop_column('user', 'salt')
    # ### end Alembic commands ###
