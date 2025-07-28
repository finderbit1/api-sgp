from pydantic import BaseModel


class Payments(BaseModel):
    id: int 
    name: str
    