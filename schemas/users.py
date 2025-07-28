from pydantic import BaseModel,EmailStr





class User(BaseModel):
    name: str
    email: EmailStr


class Vendedor(BaseModel):
    id: int
    name: str 


class Designer(BaseModel):
    id: int
    name: str



    