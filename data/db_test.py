import asyncio
from datetime import datetime

from sqlalchemy import and_, or_

from bot import dp
from data.commands import general_set
from data.models.products import ProductsOzon
from settings import config
from data.db_gino import db
from data import db_gino


async def db_test():
    await db_gino.on_startup(dp)
    from sqlalchemy import desc

    products_ozon = await ProductsOzon.query.order_by(desc(ProductsOzon.click)).where(
        ProductsOzon.click > 0).gino.all()

    for i in products_ozon:
        print(i.click)

    # print(products_ozon)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(db_test())
