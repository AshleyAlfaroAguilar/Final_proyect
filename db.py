import psycopg2
from psycopg2 import DatabaseError
from decouple import config
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column,String, INTEGER, Date, create_engine 

Base = declarative_base()

def get_connection():
    try:
        return psycopg2.connect(
            host = config('PGSLQ_HOST'),
            user = config('PGSQL_USER'),
            password = config('PGSLQ_PASSWORD'),
            database = config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex

class form(Base):
    __tablename__ = 'form'
    id= Column(INTEGER, primary_key= True)
    identify_card = Column(String, nullable= False )
    name = Column(String, nullable = False)
    direction = Column(String, nullable =False)
    gender= Column(String, nullable = False)
    phone_number = Column(String, nullable = False)
    birth_date = Column(String, nullable = False)
    career = Column(String, nullable = False)
    genre= Column(String, nullable =False)
    register_date=Column(Date, nullable=False)
    participation_date = Column(Date, nullable = False)
    age = Column(INTEGER, nullable = False)




engine = create_engine('postgresql://postgres:123456@localhost/api_form')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session=Session()