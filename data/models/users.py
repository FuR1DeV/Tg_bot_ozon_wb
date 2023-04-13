from sqlalchemy import Column, Integer, BigInteger, String, DECIMAL, sql, Text, ARRAY

from data.db_gino import BaseModel


class Users(BaseModel):
    __tablename__ = "users"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(BigInteger, nullable=False, unique=True)
    username = Column(String)
    telephone = Column(String)
    first_name = Column(String)
    last_name = Column(String)

