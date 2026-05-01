from sqlalchemy.orm import Session
from models import Remedios
from schemas import RemediosCreate, RemediosUpdate


def listar_remedios(db: Session):
    return db.query(Remedios).all()


def buscar_remedio(db: Session, remedio_id: int):
    return db.query(Remedios).filter(Remedios.id == remedio_id).first()


def criar_remedio(db: Session, dados: RemediosCreate):
    remedio = Remedios(**dados.model_dump())
    db.add(remedio)
    db.commit()
    db.refresh(remedio)
    return remedio


def atualizar_remedio(db: Session, remedio_id: int, dados: RemediosUpdate):
    remedio = buscar_remedio(db, remedio_id)

    if not remedio:
        return None

    atualizacoes = dados.model_dump(exclude_unset=True)

    for campo, valor in atualizacoes.items():
        setattr(remedio, campo, valor)

    db.commit()
    db.refresh(remedio)
    return remedio


def substituir_remedio(db: Session, remedio_id: int, dados: RemediosCreate):
    remedio = buscar_remedio(db, remedio_id)

    if not remedio:
        return None

    for campo, valor in dados.model_dump().items():
        setattr(remedio, campo, valor)

    db.commit()
    db.refresh(remedio)
    return remedio


def deletar_remedio(db: Session, remedio_id: int):
    remedio = buscar_remedio(db, remedio_id)

    if remedio:
        db.delete(remedio)
        db.commit()

    return remedio
