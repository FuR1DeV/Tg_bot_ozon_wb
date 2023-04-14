from data.models.users import Users
from data.models.products import ProductsWb, ProductsOzon
from data.models.admins import Admins


async def user_add(user_id, username, telephone, first_name, last_name):
    """Пользователь добавляется в БД"""
    user = Users(user_id=user_id, username=username, telephone=telephone, first_name=first_name,
                 last_name=last_name)
    await user.create()


async def admin_add(user_id, username, first_name, last_name):
    """Админ добавляется в БД"""
    admin = Admins(user_id=user_id, username=username, first_name=first_name, last_name=last_name)
    await admin.create()


async def product_wb_add(title, type_product, article_seller, article_product, price_spp, link):
    """Продукт WB добавляется в БД"""
    product_wb = ProductsWb(title=title, type_product=type_product, article_seller=article_seller,
                            article_product=article_product, price_spp=price_spp, link=link)
    await product_wb.create()


async def product_ozon_add(title, type_product, article_product, price, link, link_utm):
    """Продукт Ozon добавляется в БД"""
    product_ozon = ProductsOzon(title=title, type_product=type_product, article_product=article_product,
                                price=price, link=link, link_utm=link_utm)
    await product_ozon.create()


async def product_ozon_add_with_photo(title, type_product, article_product, price, link, link_utm, photo):
    """Продукт Ozon добавляется в БД"""
    product_ozon = ProductsOzon(title=title, type_product=type_product, article_product=article_product,
                                price=price, link=link, link_utm=link_utm, photo=photo)
    await product_ozon.create()


async def product_wb_add_with_photo(title, type_product, article_seller, article_product, price_spp, link, photo):
    """Продукт Wildberries добавляется в БД"""
    product_wb = ProductsWb(title=title, type_product=type_product, article_seller=article_seller,
                            article_product=article_product, price_spp=price_spp, link=link, photo=photo)
    await product_wb.create()
