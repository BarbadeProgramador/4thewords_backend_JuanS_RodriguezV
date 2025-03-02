from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root@localhost:3306/4thewords_prueba_juans_rodriguezv"
engine = create_engine(DATABASE_URL)


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        # close session 
        yield session

