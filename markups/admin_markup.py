from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


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
        get4 = InlineKeyboardButton(text='Статистика',
                                    callback_data='admin_ozon_statistics')
        get5 = InlineKeyboardButton(text='Главное Меню',
                                    callback_data='admin_main')
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(get4)
        approve_.insert(get5)
        return approve_

    @staticmethod
    def admin_check_wb():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text='Загрузить Excel WB',
                                   callback_data='admin_wb_excel')
        get1 = InlineKeyboardButton(text='Посмотреть все товары WB',
                                    callback_data='admin_wb_tg')
        get2 = InlineKeyboardButton(text='Просмотр Товара',
                                    callback_data='admin_wb_view')
        get3 = InlineKeyboardButton(text='Добавить Товар',
                                    callback_data='admin_wb_add')
        get4 = InlineKeyboardButton(text='Статистика',
                                    callback_data='admin_wb_statistics')
        get5 = InlineKeyboardButton(text='Главное Меню',
                                    callback_data='admin_main')
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(get4)
        approve_.insert(get5)
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
        get2 = InlineKeyboardButton(text='Добавить Товар',
                                    callback_data='admin_wb_add_product')
        approve_.insert(get1)
        approve_.insert(get2)
        return approve_


class AdminViewOzonMarkup:

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


class AdminViewWbMarkup:

    @staticmethod
    def admin_enter_id_wb():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='admin_wb_check')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_in_product_wb():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get0 = InlineKeyboardButton(text='Наименование',
                                    callback_data='admin_wb_change_title')
        get1 = InlineKeyboardButton(text='Категорию',
                                    callback_data='admin_wb_change_type_product')
        get2 = InlineKeyboardButton(text='Артикул Продавца',
                                    callback_data='admin_wb_change_article_seller')
        get3 = InlineKeyboardButton(text='Артикул Товара',
                                    callback_data='admin_wb_change_article_product')
        get4 = InlineKeyboardButton(text='Цену СПП',
                                    callback_data='admin_wb_change_price_spp')
        get5 = InlineKeyboardButton(text='Ссылку',
                                    callback_data='admin_wb_change_link')
        get6 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='admin_wb_change_back')
        approve_.insert(get0)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(get4)
        approve_.insert(get5)
        approve_.insert(get6)
        return approve_

    @staticmethod
    def admin_in_product_wb_back():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} Назад',
                                    callback_data='admin_in_product_wb_back')
        approve_.insert(get1)
        return approve_
