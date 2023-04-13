from sqlalchemy import Column, Integer, BigInteger, String, DECIMAL, sql, Text, ARRAY

from data.db_gino import BaseModel


class Products(BaseModel):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    type_product = Column(String, nullable=False)
    article = Column(String, nullable=False)
