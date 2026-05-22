from sqlalchemy import Column, Integer, String
from database.database import Base

class Admin(Base):

    __tablename__ = "admin_credential_database"

    id = Column(Integer, primary_key = True, index = True)

    username = Column(String, unique = True, nullable = False)

    password = Column(String, nullable = False)     #hashed password will be stored in the database, not the plain text password