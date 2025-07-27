from pydantic  import BaseModel


class Item(BaseModel):
    nome: str
    quantidade: int
    largura: str  # ou float se você estiver convertendo "1,58" → 1.58
    altura: str   # idem
    # ... outros campos
