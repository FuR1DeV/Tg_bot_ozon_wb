import csv

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

import states
from bot import bot
from markups.user_markup import UserCheckMarkup, UserViewOzonMarkup, UserViewWbMarkup
from data.commands import general_set, general_get


class UserMain:
    @staticmethod
    async def user_main(callback: types.CallbackQuery, state: FSMContext):
        await callback.message.edit_text(
            "<b>Добро пожаловать в меню Пользователя!</b>\n"
            "<b>Вы можете просмотреть товары и загружать в Excel</b>",
            reply_markup=UserCheckMarkup.user_check())
        await state.finish()


class UserCheckOzon:

    @staticmethod
    async def user_check_ozon(callback: types.CallbackQuery, state: FSMContext):
        len_products = await general_get.products_ozon_all()
        try:
            await callback.message.edit_text(text="<b>Вы в меню Ozon</b>\n"
                                                  f"<b>Кол-во товаров - {len(len_products)}</b>",
                                             reply_markup=UserCheckMarkup.user_check_ozon())
            await state.finish()
        except:
            try:
                for i in range(0, 6):
                    await bot.delete_message(callback.from_user.id, callback.message.message_id - i)
            except:
                pass
            await bot.send_message(callback.from_user.id,
                                   "<b>Вы в меню Ozon</b>\n"
                                   f"<b>Кол-во товаров - {len(len_products)}</b>",
                                   reply_markup=UserCheckMarkup.user_check_ozon())

    @staticmethod
    async def user_check_ozon_excel(callback: types.CallbackQuery):
        all_products = await general_get.products_ozon_all()
        with open("table_ozon_for_user.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "Наименование", "Категория", "Артикул товара",
                             "Цена", "Ссылка", "Ссылка UTM", "Фото"])
            for i in all_products:
                writer.writerow([i.id, i.title, i.type_product, i.article_product,
                                 i.price, i.link, i.link_utm, i.photo])
        table_ozon = InputFile("table_ozon_for_user.csv")
        await bot.send_document(chat_id=callback.from_user.id,
                                document=table_ozon)

    @staticmethod
    async def user_check_ozon_tg(callback: types.CallbackQuery, state: FSMContext):
        items = await general_get.products_ozon_all()
        book = []
        page = 1
        while True:
            for i in items:
                if int(i.id) == page:
                    try:
                        len_photo = len(i.photo)
                    except:
                        len_photo = "Фото нет!"
                    book.append(f"<b>ID</b> - <i>{i.id}</i>\n"
                                f"<b>Название</b> - <i>{i.title}</i>\n"
                                f"<b>Категория</b> - <i>{i.type_product}</i>\n"
                                f"<b>Артикул товара</b> - <i>{i.article_product}</i>\n"
                                f"<b>Цена</b> - <i>{i.price} руб.</i>\n"
                                f"<b>Ссылка с UTM</b> - <i>{i.link_utm}</i>\n"
                                f"<b>Кол-во Фото</b> - <i>{len_photo}</i>\n\n")
                    page += 1
                if len(book) == 5:
                    break
            if len(book) == 5:
                break
        await callback.message.edit_text("".join(book),
                                         disable_web_page_preview=True,
                                         reply_markup=UserCheckMarkup.user_check_next_page_ozon())
        async with state.proxy() as data:
            data["page"] = page
            data["items"] = items
            data["max_page"] = len(items)

    @staticmethod
    async def user_check_ozon_tg_next(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            page = data.get("page")
            items = data.get("items")
            book = []
            max_page = data.get("max_page")
            while True:
                for i in items:
                    if int(i.id) == page:
                        try:
                            len_photo = len(i.photo)
                        except:
                            len_photo = "Фото нет!"
                        book.append(f"<b>ID</b> - <i>{i.id}</i>\n"
                                    f"<b>Название</b> - <i>{i.title}</i>\n"
                                    f"<b>Категория</b> - <i>{i.type_product}</i>\n"
                                    f"<b>Артикул товара</b> - <i>{i.article_product}</i>\n"
                                    f"<b>Цена</b> - <i>{i.price} руб.</i>\n"
                                    f"<b>Ссылка с UTM</b> - <i>{i.link_utm}</i>\n"
                                    f"<b>Кол-во Фото</b> - <i>{len_photo}</i>\n\n")
                        page += 1
                    if len(book) == 5:
                        break
                if len(book) == 5 or max_page - page < 5:
                    break
            data["page"] = page
            if book:
                await callback.message.edit_text("".join(book),
                                                 disable_web_page_preview=True,
                                                 reply_markup=UserCheckMarkup.user_check_next_page_ozon())
            else:
                await bot.delete_message(callback.from_user.id, callback.message.message_id)
                await bot.send_message(callback.from_user.id,
                                       "<b>Больше товаров нет!</b>\n"
                                       "<b>Вы в меню Ozon</b>",
                                       reply_markup=UserCheckMarkup.user_check_ozon())


class UserCheckWb:
    @staticmethod
    async def user_check_wb(callback: types.CallbackQuery, state: FSMContext):
        len_products = await general_get.products_wb_all()
        try:
            await callback.message.edit_text(text="<b>Вы в меню Wildberries</b>\n"
                                                  f"<b>Кол-во товаров - {len(len_products)}</b>",
                                             reply_markup=UserCheckMarkup.user_check_wb())
            await state.finish()
        except:
            try:
                for i in range(0, 6):
                    await bot.delete_message(callback.from_user.id, callback.message.message_id - i)
            except:
                pass
            await bot.send_message(callback.from_user.id,
                                   "<b>Вы в меню Wildberries</b>\n"
                                   f"<b>Кол-во товаров - {len(len_products)}</b>",
                                   reply_markup=UserCheckMarkup.user_check_wb())

    @staticmethod
    async def user_check_wb_excel(callback: types.CallbackQuery):
        all_products = await general_get.products_wb_all()
        with open("table_wildberries_for_user.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "Наименование", "Категория", "Артикул продавца",
                             "Артикул товара", "Цена с учетом СПП", "Ссылка", "Фото"])
            for i in all_products:
                writer.writerow([i.id, i.title, i.type_product, i.article_seller,
                                 i.article_product, i.price_spp, i.link, i.photo])
        table_wb = InputFile("table_wildberries_for_user.csv")
        await bot.send_document(chat_id=callback.from_user.id,
                                document=table_wb)

    @staticmethod
    async def user_check_wb_tg(callback: types.CallbackQuery, state: FSMContext):
        items = await general_get.products_wb_all()
        book = []
        page = 1
        while True:
            for i in items:
                if int(i.id) == page:
                    try:
                        len_photo = len(i.photo)
                    except:
                        len_photo = "Фото нет!"
                    book.append(f"<b>ID</b> - <i>{i.id}</i>\n"
                                f"<b>Название</b> - <i>{i.title}</i>\n"
                                f"<b>Категория</b> - <i>{i.type_product}</i>\n"
                                f"<b>Артикул продавца</b> - <i>{i.article_seller}</i>\n"
                                f"<b>Артикул товара</b> - <i>{i.article_product}</i>\n"
                                f"<b>Цена с учетом СПП</b> - <i>{i.price_spp} руб.</i>\n"
                                f"<b>Ссылка</b> - <i>{i.link}</i>\n"
                                f"<b>Кол-во Фото</b> - <i>{len_photo}</i>\n\n")
                    page += 1
                if len(book) == 5:
                    break
            if len(book) == 5:
                break
        await callback.message.edit_text("".join(book),
                                         disable_web_page_preview=True,
                                         reply_markup=UserCheckMarkup.user_check_next_page_wb())
        async with state.proxy() as data:
            data["page"] = page
            data["items"] = items
            data["max_page"] = len(items)

    @staticmethod
    async def user_check_wb_tg_next(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            page = data.get("page")
            items = data.get("items")
            book = []
            max_page = data.get("max_page")
            while True:
                for i in items:
                    if int(i.id) == page:
                        try:
                            len_photo = len(i.photo)
                        except:
                            len_photo = "Фото нет!"
                        book.append(f"<b>ID</b> - <i>{i.id}</i>\n"
                                    f"<b>Название</b> - <i>{i.title}</i>\n"
                                    f"<b>Категория</b> - <i>{i.type_product}</i>\n"
                                    f"<b>Артикул продавца</b> - <i>{i.article_seller}</i>\n"
                                    f"<b>Артикул товара</b> - <i>{i.article_product}</i>\n"
                                    f"<b>Цена с учетом СПП</b> - <i>{i.price_spp} руб.</i>\n"
                                    f"<b>Ссылка</b> - <i>{i.link}</i>\n"
                                    f"<b>Кол-во Фото</b> - <i>{len_photo}</i>\n\n")
                        page += 1
                    if len(book) == 5:
                        break
                if len(book) == 5 or max_page - page < 5:
                    break
            data["page"] = page
            if book:
                await callback.message.edit_text("".join(book),
                                                 disable_web_page_preview=True,
                                                 reply_markup=UserCheckMarkup.user_check_next_page_wb())
            else:
                await bot.delete_message(callback.from_user.id, callback.message.message_id)
                await bot.send_message(callback.from_user.id,
                                       "<b>Больше товаров нет!</b>\n"
                                       "<b>Вы в меню Wildberries</b>",
                                       reply_markup=UserCheckMarkup.user_check_wb())


class UserOzonView:

    @staticmethod
    async def user_ozon_view(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите ID товара Ozon",
                                         reply_markup=UserViewOzonMarkup.user_enter_id_ozon())
        await states.UserChangeOzon.enter_id.set()

    @staticmethod
    async def user_ozon_change_back(callback: types.CallbackQuery):
        await callback.message.edit_text("<b>Вы в меню Ozon</b>",
                                         reply_markup=UserCheckMarkup.user_check_ozon())

    @staticmethod
    async def user_ozon_enter_id(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        if message.text.isdigit():
            product_id = int(message.text)
            product = await general_get.product_ozon_select(product_id)
            await state.update_data(product=product)
            if product:
                if product.photo:
                    media = types.MediaGroup()
                    for i in product.photo:
                        media.attach_photo(i)
                    await bot.send_media_group(message.from_user.id,
                                               media=media)
                    await bot.send_message(message.from_user.id,
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product.link_utm}</i>\n",
                                           reply_markup=UserViewOzonMarkup.user_in_product_ozon())
                else:
                    await bot.send_message(message.from_user.id,
                                           f"<b>Товар без Фото!</b>\n"
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product.link_utm}</i>\n",
                                           reply_markup=UserViewOzonMarkup.user_in_product_ozon())
            else:
                await bot.send_message(message.from_user.id,
                                       "Товар Ozon не найден!",
                                       reply_markup=UserCheckMarkup.user_check_ozon())
        elif not message.text.isdigit():
            await bot.send_message(message.from_user.id,
                                   "Надо ввести цифру!",
                                   reply_markup=UserCheckMarkup.user_check_ozon())


class UserWbView:

    @staticmethod
    async def user_wb_view(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите ID товара Wildberries",
                                         reply_markup=UserViewWbMarkup.user_enter_id_wb())
        await states.UserChangeWb.enter_id.set()

    @staticmethod
    async def user_wb_change_back(callback: types.CallbackQuery):
        await callback.message.edit_text("<b>Вы в меню Wildberries</b>",
                                         reply_markup=UserCheckMarkup.user_check_wb())

    @staticmethod
    async def user_wb_enter_id(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        if message.text.isdigit():
            product_id = int(message.text)
            product = await general_get.product_wb_select(product_id)
            await state.update_data(product=product)
            if product:
                if product.photo:
                    media = types.MediaGroup()
                    for i in product.photo:
                        media.attach_photo(i)
                    await bot.send_media_group(message.from_user.id,
                                               media=media)
                    await bot.send_message(message.from_user.id,
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул продавца</b> - <i>{product.article_seller}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product.price_spp} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product.link}</i>\n",
                                           reply_markup=UserViewWbMarkup.user_in_product_wb())
                else:
                    await bot.send_message(message.from_user.id,
                                           f"<b>Товар без Фото!</b>\n"
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул продавца</b> - <i>{product.article_seller}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product.price_spp} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product.link}</i>\n",
                                           reply_markup=UserViewWbMarkup.user_in_product_wb())
            else:
                await bot.send_message(message.from_user.id,
                                       "Товар Wildberries не найден!",
                                       reply_markup=UserCheckMarkup.user_check_wb())
        elif not message.text.isdigit():
            await bot.send_message(message.from_user.id,
                                   "Надо ввести цифру!",
                                   reply_markup=UserCheckMarkup.user_check_wb())
