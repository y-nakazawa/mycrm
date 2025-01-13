from datetime import datetime
from sqlmodel import SQLModel, Field


class Base(SQLModel):
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.now, nullable=False,
        sa_column_kwargs={'onupdate': datetime.now})
