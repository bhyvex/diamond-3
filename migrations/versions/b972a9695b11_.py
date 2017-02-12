"""empty message

Revision ID: b972a9695b11
Revises: None
Create Date: 2017-02-03 07:19:31.358412

"""

# revision identifiers, used by Alembic.
revision = 'b972a9695b11'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('metadata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_metadata_key_value', 'metadata', ['key', 'value'], unique=False)
    op.create_index('idx_metadata_slug', 'metadata', ['slug'], unique=False)
    op.create_index('idx_metadata_slug_key_value', 'metadata', ['slug', 'key', 'value'], unique=True)
    op.create_table('parameters',
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('key')
    )
    op.create_index('idx_parameter_key', 'parameters', ['key'], unique=True)
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.Column('payload', sa.String(), nullable=False),
    sa.Column('nonce', sa.String(), nullable=False),
    sa.Column('expiry', sa.DateTime(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_token_digest_user_id', 'tokens', ['digest', 'user_id'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('validated', sa.Boolean(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('notifications', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_user_email', 'users', ['email'], unique=True)
    op.create_index('idx_user_name', 'users', ['name'], unique=True)
    op.create_table('documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_document_active', 'documents', ['active'], unique=False)
    op.create_index('idx_document_active_user_id', 'documents', ['active', 'user_id'], unique=False)
    op.create_index('idx_document_slug', 'documents', ['slug'], unique=False)
    op.create_index('idx_document_slug_active', 'documents', ['slug', 'active'], unique=False)
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('reason', sa.String(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_notification_slug_active', 'notifications', ['slug', 'active'], unique=False)
    op.create_index('idx_notification_slug_user_id_', 'notifications', ['slug', 'user_id'], unique=True)
    op.create_index('idx_notification_user_id', 'notifications', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_notification_user_id', table_name='notifications')
    op.drop_index('idx_notification_slug_user_id_', table_name='notifications')
    op.drop_index('idx_notification_slug_active', table_name='notifications')
    op.drop_table('notifications')
    op.drop_index('idx_document_slug_active', table_name='documents')
    op.drop_index('idx_document_slug', table_name='documents')
    op.drop_index('idx_document_active_user_id', table_name='documents')
    op.drop_index('idx_document_active', table_name='documents')
    op.drop_table('documents')
    op.drop_index('idx_user_name', table_name='users')
    op.drop_index('idx_user_email', table_name='users')
    op.drop_table('users')
    op.drop_index('idx_token_digest_user_id', table_name='tokens')
    op.drop_table('tokens')
    op.drop_index('idx_parameter_key', table_name='parameters')
    op.drop_table('parameters')
    op.drop_index('idx_metadata_slug_key_value', table_name='metadata')
    op.drop_index('idx_metadata_slug', table_name='metadata')
    op.drop_index('idx_metadata_key_value', table_name='metadata')
    op.drop_table('metadata')
    # ### end Alembic commands ###