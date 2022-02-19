from sqlmodel import Session, select


def add(session: Session, *, obj_model: any, obj: any):
    db_object = obj_model.from_orm(obj)
    session.add(db_object)
    session.commit()
    session.refresh(db_object)
    return db_object


def read_all(session: Session, *, obj_model: any):
    result = session.exec(select(obj_model)).all()
    return result
