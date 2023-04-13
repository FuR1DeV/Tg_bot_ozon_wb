from sqlalchemy import Column, Integer, BigInteger, String, DECIMAL, sql

from data.db_gino import BaseModel


class Admins(BaseModel):
    __tablename__ = "admins"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(BigInteger, nullable=False, unique=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
