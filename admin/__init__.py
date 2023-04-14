__all__ = ["register_admin_handler"]

from aiogram import Dispatcher

from .admin import AdminOzon, AdminWb, AdminCheckOzon, AdminCheckWb
from states import AdminStatesOzon, AdminStatesWb


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

    disp.register_message_handler(AdminWb.title_wb,
                                  state=AdminStatesWb.title)
    disp.register_message_handler(AdminWb.type_wb,
                                  state=AdminStatesWb.type_product)
    disp.register_message_handler(AdminWb.article_seller_wb,
                                  state=AdminStatesWb.article_seller)
    disp.register_message_handler(AdminWb.article_product_wb,
                                  state=AdminStatesWb.article_product)
    disp.register_message_handler(AdminWb.price_wb,
                                  state=AdminStatesWb.price_spp)
    disp.register_message_handler(AdminWb.link_wb,
                                  state=AdminStatesWb.link)
    disp.register_message_handler(AdminWb.photo_wb,
                                  state=AdminStatesWb.photo)
    disp.register_callback_query_handler(AdminWb.wb_finish,
                                         state=["*"],
                                         text="admin_wb_done")

    disp.register_callback_query_handler(AdminCheckOzon.admin_check_ozon,
                                         state=["*"],
                                         text="admin_ozon_check")
    disp.register_callback_query_handler(AdminCheckOzon.admin_check_ozon_excel,
                                         state=["*"],
                                         text="admin_ozon_excel")
    disp.register_callback_query_handler(AdminCheckOzon.admin_check_ozon_tg,
                                         state=["*"],
                                         text="admin_ozon_tg")
    disp.register_callback_query_handler(AdminCheckOzon.admin_check_ozon_tg_next,
                                         state=["*"],
                                         text="admin_next_page_ozon")

    disp.register_callback_query_handler(AdminCheckWb.admin_check_wb,
                                         state=["*"],
                                         text="admin_wb_check")
    disp.register_callback_query_handler(AdminCheckWb.admin_check_wb_excel,
                                         state=["*"],
                                         text="admin_wb_excel")
    disp.register_callback_query_handler(AdminCheckWb.admin_check_wb_tg,
                                         state=["*"],
                                         text="admin_wb_tg")
    disp.register_callback_query_handler(AdminCheckWb.admin_check_wb_tg_next,
                                         state=["*"],
                                         text="admin_next_page_wb")
