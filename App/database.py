from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql://postgres:rad1234@10.0.0.11:5432/zincdatabase")
db_session = scoped_session(sessionmaker(bind=engine))
result = db_session.execute

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)

