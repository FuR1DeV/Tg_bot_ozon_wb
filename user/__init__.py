__all__ = ["register_user_handler"]

from aiogram import Dispatcher

from .user import UserMain, UserCheckOzon, UserCheckWb, UserOzonView, UserWbView
from states import UserChangeOzon, UserChangeWb


def register_user_handler(disp: Dispatcher):
    """User Main"""

    disp.register_callback_query_handler(UserMain.user_main,
                                         state=["*"],
                                         text="user_main")

    """User Check Ozon"""

    disp.register_callback_query_handler(UserCheckOzon.user_check_ozon,
                                         state=["*"],
                                         text="user_ozon_check")
    disp.register_callback_query_handler(UserCheckOzon.user_check_ozon_excel,
                                         state=["*"],
                                         text="user_ozon_excel")
    disp.register_callback_query_handler(UserCheckOzon.user_check_ozon_tg,
                                         state=["*"],
                                         text="user_ozon_tg")
    disp.register_callback_query_handler(UserCheckOzon.user_check_ozon_tg_next,
                                         state=["*"],
                                         text="user_next_page_ozon")
    disp.register_callback_query_handler(UserCheckOzon.user_check_ozon_tg_back,
                                         state=["*"],
                                         text="user_back_page_ozon")

    """User Check Wildberries"""

    disp.register_callback_query_handler(UserCheckWb.user_check_wb,
                                         state=["*"],
                                         text="user_wb_check")
    disp.register_callback_query_handler(UserCheckWb.user_check_wb_excel,
                                         state=["*"],
                                         text="user_wb_excel")
    disp.register_callback_query_handler(UserCheckWb.user_check_wb_tg,
                                         state=["*"],
                                         text="user_wb_tg")
    disp.register_callback_query_handler(UserCheckWb.user_check_wb_tg_next,
                                         state=["*"],
                                         text="user_next_page_wb")
    disp.register_callback_query_handler(UserCheckWb.user_check_wb_tg_back,
                                         state=["*"],
                                         text="user_back_page_wb")

    """User Ozon View"""

    disp.register_callback_query_handler(UserOzonView.user_ozon_view,
                                         state=["*"],
                                         text="user_ozon_view")
    disp.register_message_handler(UserOzonView.user_ozon_enter_id,
                                  state=UserChangeOzon.enter_id)
    disp.register_callback_query_handler(UserOzonView.user_ozon_change_back,
                                         state=["*"],
                                         text="user_ozon_change_back")

    """User Wb Change"""

    disp.register_callback_query_handler(UserWbView.user_wb_view,
                                         state=["*"],
                                         text="user_wb_view")
    disp.register_message_handler(UserWbView.user_wb_enter_id,
                                  state=UserChangeWb.enter_id)
    disp.register_callback_query_handler(UserWbView.user_wb_change_back,
                                         state=["*"],
                                         text="user_wb_change_back")
