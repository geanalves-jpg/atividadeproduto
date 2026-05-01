from sqlalchemy import Column, Integer, String, Float
from database import Base

class Remedios(Base):
    __tablename__ = "remedios"

    id          = Column(Integer, primary_key=True, index=True)
    nome        = Column(String, nullable=False)
    preco       = Column(Float, nullable=False)
    categoria   = Column(String, nullable=False)
    quantidade  = Column(Integer, nullable=False)