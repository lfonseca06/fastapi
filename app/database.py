from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.delcarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

DATABASE_URL = "postgresql://:postgres:admin@localhost:5432/ip_app"

engine = create_engine(DATABASE_URL)
SessionmLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

