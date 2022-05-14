"""initial

Revision ID: bf5585e9d96e
Revises: 
Create Date: 2022-05-14 18:04:38.249464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bf5585e9d96e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50)),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )

    op.create_table(
        "modelTypes",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(75), nullable=False),
    )

    op.create_table(
        "models",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("model_id", sa.Integer, sa.ForeignKey("userModel.id")),
        sa.Column("name", sa.String(75), nullable=False),
        sa.Column("description", sa.String(200), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )

    op.create_table(
        "userModel",
        sa.Column("user_id", sa.ForeignKey("users.id")),
        sa.Column("model_id", sa.Integer),
    )

    op.create_table(
        "modelModelType",
        sa.Column("model_id", sa.ForeignKey("model.id")),
        sa.Column("model_type_id", sa.ForeignKey("modelTypes.id")),
    )


def downgrade():
    op.drop_table("modelModelType")
    op.drop_table("userModel")
    op.drop_table("models")
    op.drop_table("modelTypes")
    op.drop_table("users")
