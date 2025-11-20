from pydantic import BaseModel, EmailStr

class UserRead(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
