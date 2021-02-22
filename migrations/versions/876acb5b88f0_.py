"""empty message

Revision ID: 876acb5b88f0
Revises: 4d8ca41fa518
Create Date: 2019-03-24 11:22:32.022366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '876acb5b88f0'
down_revision = '4d8ca41fa518'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('g_name', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('g_name')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('s_name', sa.String(length=16), nullable=True),
    sa.Column('p_age', sa.Integer(), nullable=True),
    sa.Column('s_grade_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['s_grade_id'], ['grade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('grade')
    # ### end Alembic commands ###
