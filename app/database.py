from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#DATABASE_URL = "postgresql://:postgres:admin@localhost:5432/ip_app"
DATABASE_URL = "postgresql://:elxbuvzqcg:L$oDNjJY05FLlLK2@ip-app-server.postgres.database.azure.com"
#DATABASE_URL = "cnx = psycopg2.connect(user="elxbuvzqcg", password="{your_password}", host="ip-app-server.postgres.database.azure.com", port=5432, database="ip-app")"

engine = create_engine(DATABASE_URL)
SessionmLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
