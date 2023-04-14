from data.models.users import Users
from data.models.admins import Admins
from data.models.products import ProductsWb, ProductsOzon


async def user_select(user_id):
    user = await Users.query.where(Users.user_id == user_id).gino.first()
    return user


async def admin_select(user_id):
    admin = await Admins.query.where(Admins.user_id == user_id).gino.first()
    return admin


async def products_wb_all():
    products_wb = await ProductsWb.query.gino.all()
    return products_wb


async def products_ozon_all():
    products_ozon = await ProductsOzon.query.gino.all()
    return products_ozon


async def product_ozon_select(product_id):
    product_ozon = await ProductsOzon.query.where(ProductsOzon.id == product_id).gino.first()
    return product_ozon


async def product_wb_select(product_id):
    product_wb = await ProductsWb.query.where(ProductsWb.id == product_id).gino.first()
    return product_wb
