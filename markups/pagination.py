from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from content import get_products_ozon_all_text

from settings.config import KEYBOARD

pagination_call = CallbackData("paginator", "key", "page")
show_item = CallbackData("show_item", "item_id")


def get_page_keyboard(max_pages: int, key="book", page: int = 1):
    previous_page = page - 1
    previous_page_text = f"{KEYBOARD.get('FAST_REVERSE_BUTTON')}"

    current_page = page
    current_page_text = f"{page}"

    next_page = page + 1
    next_page_text = f"{KEYBOARD.get('FAST_FORWARD_BUTTON')}"

    markup = InlineKeyboardMarkup()

    if previous_page > 0:
        markup.insert(
            InlineKeyboardButton(
                text=previous_page_text,
                callback_data=pagination_call.new(key=key,
                                                  page=previous_page)
            )
        )
    markup.insert(
        InlineKeyboardButton(
            text=current_page_text,
            callback_data=pagination_call.new(key=key, page="current_page")
        )
    )

    if next_page < max_pages:
        markup.insert(
            InlineKeyboardButton(
                text=next_page_text,
                callback_data=pagination_call.new(key=key, page=next_page)
            )
        )
    return markup


def see_all_products_markup():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(f"{KEYBOARD.get('INFORMATION')} Посмотреть все товары {KEYBOARD.get('INFORMATION')}")
    return keyboard


def admin_done_ozon():
    approve_ = InlineKeyboardMarkup()
    get = InlineKeyboardButton(text='Завершить',
                               callback_data='admin_ozon_done')
    approve_.insert(get)
    return approve_


def admin_done_wb():
    approve_ = InlineKeyboardMarkup()
    get = InlineKeyboardButton(text='Завершить',
                               callback_data='admin_wb_done')
    approve_.insert(get)
    return approve_


def admin_check():
    approve_ = InlineKeyboardMarkup()
    get = InlineKeyboardButton(text='Товары Ozon',
                               callback_data='admin_ozon_check')
    get1 = InlineKeyboardButton(text='Товары Wildberries',
                                callback_data='admin_wb_check')
    approve_.insert(get)
    approve_.insert(get1)
    return approve_


def admin_check_ozon():
    approve_ = InlineKeyboardMarkup()
    get = InlineKeyboardButton(text='Загрузить Excel Ozon',
                               callback_data='admin_ozon_excel')
    get1 = InlineKeyboardButton(text='Посмотреть все товары Ozon',
                                callback_data='admin_ozon_tg')
    approve_.insert(get)
    approve_.insert(get1)
    return approve_


def admin_check_next_page_ozon():
    approve_ = InlineKeyboardMarkup()
    get = InlineKeyboardButton(text='Следующая страница',
                               callback_data=f'admin_next_page_ozon')
    approve_.insert(get)
    return approve_


def admin_check_wb():
    approve_ = InlineKeyboardMarkup()
    get = InlineKeyboardButton(text='Загрузить Excel Wildberries',
                               callback_data='admin_wb_excel')
    get1 = InlineKeyboardButton(text='Посмотреть все товары Wildberries',
                                callback_data='admin_wb_tg')
    approve_.insert(get)
    approve_.insert(get1)
    return approve_


def admin_check_next_page_wb():
    approve_ = InlineKeyboardMarkup()
    get = InlineKeyboardButton(text='Следующая страница',
                               callback_data=f'admin_next_page_wb')
    approve_.insert(get)
    return approve_

