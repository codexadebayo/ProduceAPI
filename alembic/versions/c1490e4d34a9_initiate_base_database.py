"""Initiate Base Database

Revision ID: c1490e4d34a9
Revises: 
Create Date: 2023-10-13 12:30:38.712704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1490e4d34a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strUsername', sa.String(), nullable=False),
    sa.Column('strPassword', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('strUsername')
    )
    op.create_index(op.f('ix_admins_id'), 'admins', ['id'], unique=False)
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strCategory', sa.String(), nullable=False),
    sa.Column('strCatDescription', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('strCatDescription'),
    sa.UniqueConstraint('strCategory')
    )
    op.create_table('produce',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strProduce', sa.String(), nullable=False),
    sa.Column('strDescription', sa.String(), nullable=False),
    sa.Column('strContact', sa.String(), nullable=False),
    sa.Column('strProduceThumb', sa.String(), nullable=False),
    sa.Column('on_sale', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('strCategory', sa.String(), nullable=True),
    sa.Column('strCatDescription', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['strCatDescription'], ['categories.strCatDescription'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['strCategory'], ['categories.strCategory'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produce')
    op.drop_table('categories')
    op.drop_index(op.f('ix_admins_id'), table_name='admins')
    op.drop_table('admins')
    # ### end Alembic commands ###
