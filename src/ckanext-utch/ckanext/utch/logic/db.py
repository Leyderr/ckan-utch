from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool

DATABASE_URL = "mssql+pyodbc://consultas:Ex1w1TA4tC7*Hc^d@20.42.110.105:1433/Gestion10?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL, echo=True)
# , poolclass=QueuePool
base = declarative_base()

Session = sessionmaker(autocommit=False, bind=engine)

db_session = Session()

metadata = MetaData(bind=engine)