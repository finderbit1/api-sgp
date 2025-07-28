from pydantic import BaseModel
from typing import Optional
from decimal import Decimal



class Envio(BaseModel):
    id: int 
    name: str
    value: Optional[Decimal] = None