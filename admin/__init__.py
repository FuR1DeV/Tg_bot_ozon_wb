__all__ = ["register_admin_handler"]

from aiogram import Dispatcher

from .admin import AdminOzon
from states import AdminStatesOzon


def register_admin_handler(disp: Dispatcher):
    disp.register_message_handler(AdminOzon.title_ozon,
                                  state=AdminStatesOzon.title)
    disp.register_message_handler(AdminOzon.type_ozon,
                                  state=AdminStatesOzon.type_product)
    disp.register_message_handler(AdminOzon.article_ozon,
                                  state=AdminStatesOzon.article_product)
    disp.register_message_handler(AdminOzon.price_ozon,
                                  state=AdminStatesOzon.price)
    disp.register_message_handler(AdminOzon.link_ozon,
                                  state=AdminStatesOzon.link)
    disp.register_message_handler(AdminOzon.link_utm_ozon,
                                  state=AdminStatesOzon.link_utm)
    disp.register_message_handler(AdminOzon.photo_ozon,
                                  state=AdminStatesOzon.photo)
    disp.register_callback_query_handler(AdminOzon.ozon_finish,
                                         state=["*"],
                                         text="admin_ozon_done")
