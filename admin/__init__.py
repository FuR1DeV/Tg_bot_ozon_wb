__all__ = ["register_admin_handler"]

from aiogram import Dispatcher

import states
from .admin import AdminCheckOzon, AdminCheckWb, AdminMain, \
    AdminOzonAddProduct, AdminWbAddProduct, AdminOzonView
from states import AdminStatesOzon, AdminStatesWb, AdminChangeOzon


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

    """Admin Ozon Add Product"""

    disp.register_callback_query_handler(AdminWbAddProduct.admin_wb_add_product,
                                         state=["*"],
                                         text="admin_wb_add")
    disp.register_message_handler(AdminWbAddProduct.title_wb,
                                  state=AdminStatesWb.title)
    disp.register_message_handler(AdminWbAddProduct.type_wb,
                                  state=AdminStatesWb.type_product)
    disp.register_message_handler(AdminWbAddProduct.article_seller_wb,
                                  state=AdminStatesWb.article_seller)
    disp.register_message_handler(AdminWbAddProduct.article_product_wb,
                                  state=AdminStatesWb.article_product)
    disp.register_message_handler(AdminWbAddProduct.price_spp_wb,
                                  state=AdminStatesWb.price_spp)
    disp.register_message_handler(AdminWbAddProduct.link_wb,
                                  state=AdminStatesWb.link)
    disp.register_message_handler(AdminWbAddProduct.photo_wb_1,
                                  state=AdminStatesWb.photo_wb_1,
                                  content_types=["photo"])
    disp.register_message_handler(AdminWbAddProduct.photo_wb_2,
                                  state=AdminStatesWb.photo_wb_2,
                                  content_types=["photo"])
    disp.register_message_handler(AdminWbAddProduct.photo_wb_3,
                                  state=AdminStatesWb.photo_wb_3,
                                  content_types=["photo"])
    disp.register_callback_query_handler(AdminWbAddProduct.wb_finish,
                                         state=["*"],
                                         text="admin_wb_add_product")

    """Admin Ozon Change"""

    disp.register_callback_query_handler(AdminOzonView.admin_ozon_view,
                                         state=["*"],
                                         text="admin_ozon_view")
    disp.register_message_handler(AdminOzonView.admin_ozon_enter_id,
                                  state=states.AdminChangeOzon)
    disp.register_callback_query_handler(AdminOzonView.admin_ozon_change_back,
                                         state=["*"],
                                         text="admin_ozon_change_back")
