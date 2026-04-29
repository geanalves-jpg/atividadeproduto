from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import Remedios
import crud
from database import Base, engine, get_db
from schemas import RemediosCreate, RemediosResponse, RemediosUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Remedios")

@app.get("/remedios")
def listar_remedios(db: Session = Depends(get_db)):
    remedios = db.query(Remedios).all()
    return remedios

@app.get("/remedios/{remedios_id}")
def buscar_remedios(remedios_id: int, db: Session = Depends(get_db)):
    remedios = db.query(Remedios).filter(Remedios.id == remedios_id).first()

    if not remedios:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")

    return remedios

@app.post("/remedios", response_model=RemediosResponse, status_code=201)
def criar_remedio(dados: RemediosCreate, db: Session = Depends(get_db)):
    return crud.criar_remedio(db, dados)

@app.delete("/remedios/{remedio_id}", status_code=204)
def deletar_remedio(remedio_id: int, db: Session = Depends(get_db)):
    return crud.deletar_remedio(db, remedio_id) 

@app.put("/remedios/{remedio_id}", response_model=RemediosResponse)
def atualizar_remedio(remedio_id: int, dados: RemediosCreate, db: Session = Depends(get_db)):
    return crud.atualizar_remedio(db, remedio_id, dados)

@app.patch("/remedios/{remedio_id}", response_model=RemediosResponse)
def atualizar_parcial(remedio_id: int, dados: RemediosUpdate, db: Session = Depends(get_db)):
    return crud.atualizar_parcial(db, remedio_id, dados)