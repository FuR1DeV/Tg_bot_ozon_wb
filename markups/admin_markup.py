from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from content import get_products_ozon_all_text

from settings.config import KEYBOARD

pagination_call = CallbackData("paginator", "key", "page")
show_item = CallbackData("show_item", "item_id")


# def get_page_keyboard(max_pages: int, key="book", page: int = 1):
#     previous_page = page - 1
#     previous_page_text = f"{KEYBOARD.get('FAST_REVERSE_BUTTON')}"
#
#     current_page = page
#     current_page_text = f"{page}"
#
#     next_page = page + 1
#     next_page_text = f"{KEYBOARD.get('FAST_FORWARD_BUTTON')}"
#
#     markup = InlineKeyboardMarkup()
#
#     if previous_page > 0:
#         markup.insert(
#             InlineKeyboardButton(
#                 text=previous_page_text,
#                 callback_data=pagination_call.new(key=key,
#                                                   page=previous_page)
#             )
#         )
#     markup.insert(
#         InlineKeyboardButton(
#             text=current_page_text,
#             callback_data=pagination_call.new(key=key, page="current_page")
#         )
#     )
#
#     if next_page < max_pages:
#         markup.insert(
#             InlineKeyboardButton(
#                 text=next_page_text,
#                 callback_data=pagination_call.new(key=key, page=next_page)
#             )
#         )
#     return markup
#
#
# def see_all_products_markup():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.row(f"{KEYBOARD.get('INFORMATION')} Посмотреть все товары {KEYBOARD.get('INFORMATION')}")
#     return keyboard

class AdminCheckMarkup:

    @staticmethod
    def admin_check():
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Товары Ozon',
                                   callback_data='admin_ozon_check')
        get1 = InlineKeyboardButton(text='Товары Wildberries',
                                    callback_data='admin_wb_check')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_check_ozon():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text='Загрузить Excel',
                                   callback_data='admin_ozon_excel')
        get1 = InlineKeyboardButton(text='Посмотреть все Товары',
                                    callback_data='admin_ozon_tg')
        get2 = InlineKeyboardButton(text='Просмотр Товара',
                                    callback_data='admin_ozon_view')
        get3 = InlineKeyboardButton(text='Добавить Товар',
                                    callback_data='admin_ozon_add')
        get4 = InlineKeyboardButton(text='Главное Меню',
                                    callback_data='admin_main')
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(get4)
        return approve_

    @staticmethod
    def admin_check_wb():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text='Загрузить Excel WB',
                                   callback_data='admin_wb_excel')
        get1 = InlineKeyboardButton(text='Посмотреть все товары WB',
                                    callback_data='admin_wb_tg')
        get2 = InlineKeyboardButton(text='Просмотр Товара',
                                    callback_data='admin_wb_change')
        get3 = InlineKeyboardButton(text='Добавить Товар',
                                    callback_data='admin_wb_add')
        get4 = InlineKeyboardButton(text='Главное Меню',
                                    callback_data='admin_main')
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(get4)
        return approve_

    @staticmethod
    def admin_check_next_page_ozon():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text='Следующая страница',
                                   callback_data=f'admin_next_page_ozon')
        get1 = InlineKeyboardButton(text='Назад',
                                    callback_data=f'admin_ozon_check')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_check_next_page_wb():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text='Следующая страница',
                                   callback_data=f'admin_next_page_wb')
        get1 = InlineKeyboardButton(text='Назад',
                                    callback_data=f'admin_wb_check')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_


class AdminAddMarkup:

    @staticmethod
    def admin_add_ozon():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text='Назад',
                                    callback_data='admin_ozon_check')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_add_ozon_finish():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Отмена',
                                    callback_data='admin_ozon_check')
        get2 = InlineKeyboardButton(text='Добавить Товар',
                                    callback_data='admin_ozon_add_product')
        approve_.insert(get1)
        approve_.insert(get2)
        return approve_

    @staticmethod
    def admin_add_wb():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text='Назад',
                                    callback_data='admin_wb_check')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_add_wb_finish():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Отмена',
                                    callback_data='admin_wb_check')
        get2 = InlineKeyboardButton(text='Добавить',
                                    callback_data='admin_wb_add_product')
        approve_.insert(get1)
        approve_.insert(get2)
        return approve_


class AdminViewMarkup:

    @staticmethod
    def admin_enter_id_ozon():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='admin_ozon_check')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_in_product_ozon():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get0 = InlineKeyboardButton(text='Наименование',
                                    callback_data='admin_ozon_change_title')
        get1 = InlineKeyboardButton(text='Категорию',
                                    callback_data='admin_ozon_change_type_product')
        get2 = InlineKeyboardButton(text='Артикул',
                                    callback_data='admin_ozon_change_article_product')
        get3 = InlineKeyboardButton(text='Цену',
                                    callback_data='admin_ozon_change_price')
        get4 = InlineKeyboardButton(text='Ссылку UTM',
                                    callback_data='admin_ozon_change_link_utm')
        get5 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='admin_ozon_change_back')
        approve_.insert(get0)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(get4)
        approve_.insert(get5)
        return approve_

    @staticmethod
    def admin_in_product_ozon_back():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='admin_in_product_ozon_back')
        approve_.insert(get1)
        return approve_
