from pydantic import BaseModel
from typing import List

class Payments(BaseModel):
    id: int 
    name: str
    