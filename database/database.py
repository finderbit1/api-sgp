
from sqlmodel import SQLModel, create_engine, Session
from sqlmodel.pool import StaticPool

DATABASE_URL = "sqlite:///db/banco.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

def create_db_and_tables():
    """Cria as tabelas no banco de dados"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependência para injetar sessão nas rotas"""
    with Session(engine) as session:
        yield session