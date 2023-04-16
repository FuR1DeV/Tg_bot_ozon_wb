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
    """Продукт Ozon добавляется в БД с Фото"""
    product_ozon = ProductsOzon(title=title, type_product=type_product, article_product=article_product,
                                price=price, link=link, link_utm=link_utm, photo=photo)
    await product_ozon.create()


async def product_wb_add_with_photo(title, type_product, article_seller, article_product, price_spp, link, photo):
    """Продукт Wildberries добавляется в БД с Фото"""
    product_wb = ProductsWb(title=title, type_product=type_product, article_seller=article_seller,
                            article_product=article_product, price_spp=price_spp, link=link, photo=photo)
    await product_wb.create()


async def product_ozon_click(product_id):
    """Кликнули на продукт Ozon"""
    product_ozon = await ProductsOzon.query.where(ProductsOzon.id == product_id).gino.first()
    await product_ozon.update(click=product_ozon.click + 1).apply()


async def product_wb_click(product_id):
    """Кликнули на продукт Wildberries"""
    product_wb = await ProductsWb.query.where(ProductsWb.id == product_id).gino.first()
    await product_wb.update(click=product_wb.click + 1).apply()


async def product_ozon_add_photo(product_id, photo_id):
    """Добавляется Фото для Ozon"""
    product_ozon = await ProductsOzon.query.where(ProductsOzon.id == product_id).gino.first()
    if product_ozon.photo is None:
        result = [photo_id]
        await product_ozon.update(photo=result).apply()
        return False
    else:
        if len(product_ozon.photo) >= 3:
            return True
        else:
            result = product_ozon.photo
            result.append(photo_id)
            await product_ozon.update(photo=result).apply()
            return False


async def product_ozon_change_title(product_id, new_title):
    """Обновляется наименование товара Ozon"""
    product_ozon = await ProductsOzon.query.where(ProductsOzon.id == product_id).gino.first()
    await product_ozon.update(title=new_title).apply()


async def product_ozon_change_type_product(product_id, new_type_product):
    """Обновляется Категория товара Ozon"""
    product_ozon = await ProductsOzon.query.where(ProductsOzon.id == product_id).gino.first()
    await product_ozon.update(type_product=new_type_product).apply()


async def product_ozon_change_article_product(product_id, new_article_product):
    """Обновляется Артикул товара Ozon"""
    product_ozon = await ProductsOzon.query.where(ProductsOzon.id == product_id).gino.first()
    await product_ozon.update(article_product=int(new_article_product)).apply()


async def product_ozon_change_price(product_id, new_price):
    """Обновляется Цена товара Ozon"""
    product_ozon = await ProductsOzon.query.where(ProductsOzon.id == product_id).gino.first()
    await product_ozon.update(price=int(new_price)).apply()


async def product_ozon_change_link_utm(product_id, new_link_utm):
    """Обновляется Ссылка UTM товара Ozon"""
    product_ozon = await ProductsOzon.query.where(ProductsOzon.id == product_id).gino.first()
    await product_ozon.update(link_utm=new_link_utm).apply()
