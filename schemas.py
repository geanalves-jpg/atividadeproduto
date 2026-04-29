from typing import Optional
from pydantic import BaseModel, ConfigDict

class RemediosCreate(BaseModel):
    nome:    str
    preco: float
    categoria: str = ""
    quantidade: int
    
class RemediosResponse(BaseModel):
    id:        int
    nome:    str
    preco: float
    categoria: str
    quantidade: int

    model_config = ConfigDict(from_attributes=True)

class RemediosUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] 
    categoria: Optional[str]
    quantidade: Optional[int] = None
    
    
