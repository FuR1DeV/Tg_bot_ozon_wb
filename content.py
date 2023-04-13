from data.commands import general_get


async def get_products_ozon_all():
    items = await general_get.products_ozon_all()
    return items


async def get_products_ozon_all_text() -> list:
    items = await general_get.products_ozon_all()
    book = []
    for i in items:
        text = f"<b>ID</b> - <i>{i.id}</i>\n" \
               f"<b>Название</b> - <i>{i.title}</i>\n" \
               f"<b>Категория</b> - <i>{i.type_product}</i>\n" \
               f"<b>Артикль товара</b> - <i>{i.article_product}</i>\n" \
               f"<b>Цена</b> - <i>{i.price} руб.</i>\n" \
               f"<b>Ссылка</b> - <i>{i.link_utm}</i>\n"
        book.append(text)
    book.insert(0, book.pop(-1))
    return book


async def get_item_ozon(item_id):
    items = await get_products_ozon_all()
    for item in items:
        if int(item_id) == item.id:
            return item


async def get_page_ozon(page: int = 1):
    page_index = page - 1
    book = await get_products_ozon_all_text()
    return book[page_index]

