import sqlalchemy as sa
from sqlmodel import Session, create_engine, SQLModel


def setup_guids_postgresql(engine) -> None:
    with Session(engine) as session:
        session.execute('create EXTENSION if not EXISTS "pgcrypto"')
        session.commit()


def create_db_and_tables(engine):
    # SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


GUID_SERVER_DEFAULT_POSTGRESQL = sa.DefaultClause(sa.text("gen_random_uuid()"))

postgres_url = f"postgresql://postgres:postgres@localhost/testlocal"

engine = create_engine(postgres_url, echo=True, pool_pre_ping=True)
setup_guids_postgresql(engine)
