from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


class UserCheckMarkup:

    @staticmethod
    def user_check():
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Товары Ozon',
                                   callback_data='user_ozon_check')
        get1 = InlineKeyboardButton(text='Товары Wildberries',
                                    callback_data='user_wb_check')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def user_check_next_page_ozon():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text='Следующая страница',
                                   callback_data=f'user_next_page_ozon')
        get1 = InlineKeyboardButton(text='Назад',
                                    callback_data=f'user_ozon_check')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def user_check_ozon():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text='Загрузить Excel',
                                   callback_data='user_ozon_excel')
        get1 = InlineKeyboardButton(text='Посмотреть все Товары',
                                    callback_data='user_ozon_tg')
        get2 = InlineKeyboardButton(text='Просмотр Товара',
                                    callback_data='user_ozon_view')
        get4 = InlineKeyboardButton(text='Главное Меню',
                                    callback_data='user_main')
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get4)
        return approve_

    @staticmethod
    def user_check_wb():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text='Загрузить Excel WB',
                                   callback_data='user_wb_excel')
        get1 = InlineKeyboardButton(text='Посмотреть все товары WB',
                                    callback_data='user_wb_tg')
        get2 = InlineKeyboardButton(text='Просмотр Товара',
                                    callback_data='user_wb_view')
        get4 = InlineKeyboardButton(text='Главное Меню',
                                    callback_data='user_main')
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get4)
        return approve_

    @staticmethod
    def user_check_next_page_wb():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text='Следующая страница',
                                   callback_data=f'user_next_page_wb')
        get1 = InlineKeyboardButton(text='Назад',
                                    callback_data=f'user_wb_check')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_


class UserViewOzonMarkup:

    @staticmethod
    def user_enter_id_ozon():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='user_ozon_check')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def user_in_product_ozon():
        approve_ = InlineKeyboardMarkup()
        get5 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='user_ozon_change_back')
        approve_.insert(get5)
        return approve_

    @staticmethod
    def user_in_product_ozon_back():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='user_in_product_ozon_back')
        approve_.insert(get1)
        return approve_


class UserViewWbMarkup:

    @staticmethod
    def user_enter_id_wb():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='user_wb_check')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def user_in_product_wb():
        approve_ = InlineKeyboardMarkup()
        get6 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='user_wb_change_back')
        approve_.insert(get6)
        return approve_

    @staticmethod
    def user_in_product_wb_back():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='user_in_product_wb_back')
        approve_.insert(get1)
        return approve_
