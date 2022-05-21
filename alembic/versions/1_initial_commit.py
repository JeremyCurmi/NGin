"""initial

Revision ID: bf5585e9d96e
Revises: 
Create Date: 2022-05-14 18:04:38.249464

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("full_name", sa.String(50)),
        sa.Column("email", sa.String(100), nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=True),
        sa.Column("updated_at", sa.DateTime, nullable=True),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=True)

    op.create_table(
        "modelType",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(75), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=True),
    )

    op.create_table(
        "model",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("model_id", sa.Integer),
        sa.Column("name", sa.String(75), nullable=False),
        sa.Column("description", sa.String(200), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=True),
    )

    op.create_table(
        "userModel",
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id"), onupdate="CASCADE"),
        sa.Column(
            "model_id", sa.Integer, sa.ForeignKey("model.id"), onupdate="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.ForeignKeyConstraint(["model_id"], ["model.id"]),
        sa.PrimaryKeyConstraint("user_id", "model_id"),
    )

    op.create_table(
        "modelModelType",
        sa.Column(
            "model_id", sa.Integer, sa.ForeignKey("model.id"), onupdate="CASCADE"
        ),
        sa.Column(
            "model_type_id",
            sa.Integer,
            sa.ForeignKey("modelType.id"),
            onupdate="CASCADE",
        ),
        sa.PrimaryKeyConstraint("model_id", "model_type_id"),
    )

    op.create_table(
        "modelVersion",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("model_version_id", sa.Integer),
        sa.Column("description", sa.String(200), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=True),
    )

    op.create_table(
        "modelModelVersion",
        sa.Column(
            "model_id", sa.Integer, sa.ForeignKey("model.id"), onupdate="CASCADE"
        ),
        sa.Column(
            "model_version_id",
            sa.Integer,
            sa.ForeignKey("modelVersion.id"),
            onupdate="CASCADE",
        ),
        sa.PrimaryKeyConstraint("model_id", "model_version_id"),
    )


def downgrade():
    op.drop_table("modelModelVersion")
    op.drop_table("modelVersion")
    op.drop_table("modelModelType")
    op.drop_table("userModel")
    op.drop_table("model")
    op.drop_table("modelType")
    op.drop_table("user")
