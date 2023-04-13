from sqlalchemy import Column, Integer, BigInteger, String, DECIMAL, sql, Text, ARRAY

from data.db_gino import BaseModel


class ProductsWb(BaseModel):
    __tablename__ = "products_wb"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    type_product = Column(String, nullable=False)
    article_seller = Column(String, nullable=False)
    article_product = Column(BigInteger, nullable=False)
    price_spp = Column(Integer, nullable=False)
    link = Column(String, nullable=False)
    photo = Column(ARRAY(String))
    click = Column(Integer, server_default="0")


class ProductsOzon(BaseModel):
    __tablename__ = "products_ozon"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    type_product = Column(String, nullable=False)
    article_product = Column(BigInteger, nullable=False)
    price = Column(Integer, nullable=False)
    link = Column(String, nullable=False)
    link_utm = Column(String, nullable=False)
    photo = Column(ARRAY(String))
    click = Column(Integer, server_default="0")
