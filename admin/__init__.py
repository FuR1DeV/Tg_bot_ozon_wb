__all__ = ["register_admin_handler"]

from aiogram import Dispatcher

from .admin import AdminCheckOzon, AdminCheckWb, AdminMain, AdminOzonAddProduct
from states import AdminStatesOzon, AdminStatesWb


def register_admin_handler(disp: Dispatcher):
    """Admin Main"""

    disp.register_callback_query_handler(AdminMain.admin_main,
                                         state=["*"],
                                         text="admin_main")

    """Admin Check Ozon"""

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

    """Admin Check Wildberries"""

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

    """Admin Ozon Add Product"""

    disp.register_callback_query_handler(AdminOzonAddProduct.admin_ozon_add_product,
                                         state=["*"],
                                         text="admin_ozon_add")
    disp.register_message_handler(AdminOzonAddProduct.title_ozon,
                                  state=AdminStatesOzon.title)
    disp.register_message_handler(AdminOzonAddProduct.type_ozon,
                                  state=AdminStatesOzon.type_product)
    disp.register_message_handler(AdminOzonAddProduct.article_ozon,
                                  state=AdminStatesOzon.article_product)
    disp.register_message_handler(AdminOzonAddProduct.price_ozon,
                                  state=AdminStatesOzon.price)
    disp.register_message_handler(AdminOzonAddProduct.link_utm_ozon,
                                  state=AdminStatesOzon.link_utm)
    disp.register_message_handler(AdminOzonAddProduct.photo_ozon_1,
                                  state=AdminStatesOzon.photo_ozon_1,
                                  content_types=["photo"])
    disp.register_message_handler(AdminOzonAddProduct.photo_ozon_2,
                                  state=AdminStatesOzon.photo_ozon_2,
                                  content_types=["photo"])
    disp.register_message_handler(AdminOzonAddProduct.photo_ozon_3,
                                  state=AdminStatesOzon.photo_ozon_3,
                                  content_types=["photo"])
    disp.register_callback_query_handler(AdminOzonAddProduct.ozon_finish,
                                         state=["*"],
                                         text="admin_ozon_add_product")
