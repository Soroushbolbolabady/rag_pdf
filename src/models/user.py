from pydantic import EmailStr
from sqlmodel import SQLModel , Field
import uuid
from datetime import datetime

class User(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(index = True, nullable= False)
    hashed_password: str = Field(nullable=False)
    created_at: str = Field(default_factory=datetime.now,nullable= False )
