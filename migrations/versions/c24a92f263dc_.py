"""empty message

Revision ID: c24a92f263dc
Revises: 08d9220ee3ec
Create Date: 2022-05-29 18:18:31.498734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c24a92f263dc'
down_revision = '08d9220ee3ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('data_nascimento', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('data_ultima_doacao', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'data_ultima_doacao')
    op.drop_column('users', 'data_nascimento')
    # ### end Alembic commands ###
