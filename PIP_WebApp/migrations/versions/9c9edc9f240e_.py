"""empty message

Revision ID: 9c9edc9f240e
Revises: 
Create Date: 2021-09-17 12:05:25.278649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c9edc9f240e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'course', 'marksheet', ['marksheet_id'], ['id'])
    op.create_foreign_key(None, 'student', 'stream', ['stream_id'], ['id'])
    op.create_foreign_key(None, 'student', 'college', ['college_id'], ['id'])
    op.drop_column('student', 'college')
    op.drop_column('student', 'stream')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('stream', sa.VARCHAR(length=255), nullable=True))
    op.add_column('student', sa.Column('college', sa.VARCHAR(length=255), nullable=True))
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'course', type_='foreignkey')
    # ### end Alembic commands ###
