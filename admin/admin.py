import csv

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

import states
from bot import bot
from markups.admin_markup import AdminCheckMarkup, AdminAddMarkup, AdminViewOzonMarkup, AdminViewWbMarkup
from data.commands import general_set, general_get


class AdminMain:
    @staticmethod
    async def admin_main(callback: types.CallbackQuery, state: FSMContext):
        await callback.message.edit_text(
            "<b>Добро пожаловать в меню Администратора</b>\n"
            "<b>Вы можете просмотреть товары, загружать в Excel, редактировать и добавлять новые</b>",
            reply_markup=AdminCheckMarkup.admin_check())
        await state.finish()


class AdminCheckOzon:
    @staticmethod
    async def admin_check_ozon(callback: types.CallbackQuery, state: FSMContext):
        len_products = await general_get.products_ozon_all()
        try:
            await callback.message.edit_text(text="<b>Вы в меню Ozon</b>\n"
                                                  f"<b>Кол-во товаров - {len(len_products)}</b>",
                                             reply_markup=AdminCheckMarkup.admin_check_ozon())
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
                                   reply_markup=AdminCheckMarkup.admin_check_ozon())

    @staticmethod
    async def admin_check_ozon_excel(callback: types.CallbackQuery):
        all_products = await general_get.products_ozon_all()
        with open("table_ozon.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "Наименование", "Категория", "Артикул товара",
                             "Цена", "Ссылка", "Ссылка UTM", "Фото", "Клики"])
            for i in all_products:
                writer.writerow([i.id, i.title, i.type_product, i.article_product,
                                 i.price, i.link, i.link_utm, i.photo, i.click])
        table_ozon = InputFile("table_ozon.csv")
        await bot.send_document(chat_id=callback.from_user.id,
                                document=table_ozon)

    @staticmethod
    async def admin_check_ozon_tg(callback: types.CallbackQuery, state: FSMContext):
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
                                f"<b>Кол-во Фото</b> - <i>{len_photo}</i>\n"
                                f"<b>Клики</b> - <i>{i.click}</i>\n\n")
                    page += 1
                if len(book) == 5:
                    break
            if len(book) == 5:
                break
        await callback.message.edit_text("".join(book),
                                         disable_web_page_preview=True,
                                         reply_markup=AdminCheckMarkup.admin_check_next_page_ozon())
        async with state.proxy() as data:
            data["page"] = page
            data["items"] = items
            data["max_page"] = len(items)

    @staticmethod
    async def admin_check_ozon_tg_next(callback: types.CallbackQuery, state: FSMContext):
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
                                    f"<b>Кол-во Фото</b> - <i>{len_photo}</i>\n"
                                    f"<b>Клики</b> - <i>{i.click}</i>\n\n")
                        page += 1
                    if len(book) == 5:
                        break
                if len(book) == 5 or max_page - page < 5:
                    break
            data["page"] = page
            if book:
                await callback.message.edit_text("".join(book),
                                                 disable_web_page_preview=True,
                                                 reply_markup=AdminCheckMarkup.admin_check_next_page_ozon())
            else:
                await bot.delete_message(callback.from_user.id, callback.message.message_id)
                await bot.send_message(callback.from_user.id,
                                       "<b>Больше товаров нет!</b>\n"
                                       "<b>Вы в меню Ozon</b>",
                                       reply_markup=AdminCheckMarkup.admin_check_ozon())


class AdminCheckWb:
    @staticmethod
    async def admin_check_wb(callback: types.CallbackQuery, state: FSMContext):
        len_products = await general_get.products_wb_all()
        try:
            await callback.message.edit_text(text="<b>Вы в меню Wildberries</b>\n"
                                                  f"<b>Кол-во товаров - {len(len_products)}</b>",
                                             reply_markup=AdminCheckMarkup.admin_check_wb())
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
                                   reply_markup=AdminCheckMarkup.admin_check_wb())

    @staticmethod
    async def admin_check_wb_excel(callback: types.CallbackQuery):
        all_products = await general_get.products_wb_all()
        with open("table_wildberries.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "Наименование", "Категория", "Артикул продавца",
                             "Артикул товара", "Цена с учетом СПП", "Ссылка", "Фото", "Клики"])
            for i in all_products:
                writer.writerow([i.id, i.title, i.type_product, i.article_seller,
                                 i.article_product, i.price_spp, i.link, i.photo, i.click])
        table_wb = InputFile("table_wildberries.csv")
        await bot.send_document(chat_id=callback.from_user.id,
                                document=table_wb)

    @staticmethod
    async def admin_check_wb_tg(callback: types.CallbackQuery, state: FSMContext):
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
                                f"<b>Кол-во Фото</b> - <i>{len_photo}</i>\n"
                                f"<b>Клики</b> - <i>{i.click}</i>\n\n")
                    page += 1
                if len(book) == 5:
                    break
            if len(book) == 5:
                break
        await callback.message.edit_text("".join(book),
                                         disable_web_page_preview=True,
                                         reply_markup=AdminCheckMarkup.admin_check_next_page_wb())
        async with state.proxy() as data:
            data["page"] = page
            data["items"] = items
            data["max_page"] = len(items)

    @staticmethod
    async def admin_check_wb_tg_next(callback: types.CallbackQuery, state: FSMContext):
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
                                    f"<b>Кол-во Фото</b> - <i>{len_photo}</i>\n"
                                    f"<b>Клики</b> - <i>{i.click}</i>\n\n")
                        page += 1
                    if len(book) == 5:
                        break
                if len(book) == 5 or max_page - page < 5:
                    break
            data["page"] = page
            if book:
                await callback.message.edit_text("".join(book),
                                                 disable_web_page_preview=True,
                                                 reply_markup=AdminCheckMarkup.admin_check_next_page_wb())
            else:
                await bot.delete_message(callback.from_user.id, callback.message.message_id)
                await bot.send_message(callback.from_user.id,
                                       "<b>Больше товаров нет!</b>\n"
                                       "<b>Вы в меню Wildberries</b>",
                                       reply_markup=AdminCheckMarkup.admin_check_wb())


class AdminOzonAddProduct:

    @staticmethod
    async def admin_ozon_add_product(callback: types.CallbackQuery):
        await callback.message.edit_text("Добавляем товар из Ozon\n"
                                         "Введите <b>Наименование</b>",
                                         reply_markup=AdminAddMarkup.admin_add_ozon())
        await states.AdminStatesOzon.title.set()

    @staticmethod
    async def title_ozon(message: types.Message, state: FSMContext):
        if message.text:
            await state.update_data(title=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите Категорию товара</b>",
                                   reply_markup=AdminAddMarkup.admin_add_ozon())
            await states.AdminStatesOzon.next()

    @staticmethod
    async def type_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
        if message.text:
            await state.update_data(type_product=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите Артикул</b>",
                                   reply_markup=AdminAddMarkup.admin_add_ozon())
            await states.AdminStatesOzon.next()

    @staticmethod
    async def article_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
        if message.text.isdigit():
            await state.update_data(article_product=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите цену</b>",
                                   reply_markup=AdminAddMarkup.admin_add_ozon())
            await states.AdminStatesOzon.next()
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Артикул должен быть цифрой</b>",
                                   reply_markup=AdminAddMarkup.admin_add_ozon())

    @staticmethod
    async def price_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_product = data.get("article_product")
        if message.text.isdigit():
            await state.update_data(price=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите ссылку UTM</b>",
                                   reply_markup=AdminAddMarkup.admin_add_ozon(),
                                   disable_web_page_preview=True)
            await states.AdminStatesOzon.next()
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Цена должна быть цифрой!</b>",
                                   reply_markup=AdminAddMarkup.admin_add_ozon())

    @staticmethod
    async def link_utm_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_product = data.get("article_product")
            price = data.get("price")
            data["photo"] = []
        if message.text:
            await state.update_data(link_utm=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{price}</i>\n"
                                   f"<b>Ссылка UTM</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь добавьте Фото (Фото добавляется по одной)</b>",
                                   reply_markup=AdminAddMarkup.admin_add_ozon(),
                                   disable_web_page_preview=True)
            await states.AdminStatesOzon.next()

    @staticmethod
    async def photo_ozon_1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_product = data.get("article_product")
            price = data.get("price")
            link_utm = data.get("link_utm")
        if message.photo:
            async with state.proxy() as data:
                data.get("photo").append(message.photo[2].file_id)
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
        text = f"<b>Наименование</b> - <i>{title}</i>\n" \
               f"<b>Категория</b> - <i>{type_product}</i>\n" \
               f"<b>Артикул товара</b> - <i>{article_product}</i>\n" \
               f"<b>Цена</b> - <i>{price}</i>\n" \
               f"<b>Ссылка UTM</b> - <i>{link_utm}</i>\n\n" \
               f"<b>У вас 1 Фотография, Вы можете еще добавить 2</b>"
        await message.answer_photo(message.photo[2].file_id,
                                   caption=text,
                                   reply_markup=AdminAddMarkup.admin_add_ozon_finish())
        await states.AdminStatesOzon.next()

    @staticmethod
    async def photo_ozon_2(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_product = data.get("article_product")
            price = data.get("price")
            link_utm = data.get("link_utm")
            if message.photo:
                data.get("photo").append(message.photo[2].file_id)
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
            text = f"<b>Наименование</b> - <i>{title}</i>\n" \
                   f"<b>Категория</b> - <i>{type_product}</i>\n" \
                   f"<b>Артикул товара</b> - <i>{article_product}</i>\n" \
                   f"<b>Цена</b> - <i>{price}</i>\n" \
                   f"<b>Ссылка UTM</b> - <i>{link_utm}</i>\n\n" \
                   f"<b>У вас 2 Фотографии, можете добавить еще 1</b>"
            media = types.MediaGroup()
            for i in data.get("photo"):
                media.attach_photo(i)
            await bot.send_media_group(message.from_user.id,
                                       media=media)
            await bot.send_message(message.from_user.id,
                                   text,
                                   reply_markup=AdminAddMarkup.admin_add_ozon_finish(),
                                   disable_web_page_preview=True)
            await states.AdminStatesOzon.next()

    @staticmethod
    async def photo_ozon_3(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_product = data.get("article_product")
            price = data.get("price")
            link_utm = data.get("link_utm")
            if message.photo:
                data.get("photo").append(message.photo[2].file_id)
                try:
                    for i in range(0, 6):
                        await bot.delete_message(message.from_user.id, message.message_id - i)
                except:
                    pass
            text = f"<b>Наименование</b> - <i>{title}</i>\n" \
                   f"<b>Категория</b> - <i>{type_product}</i>\n" \
                   f"<b>Артикул товара</b> - <i>{article_product}</i>\n" \
                   f"<b>Цена</b> - <i>{price}</i>\n" \
                   f"<b>Ссылка UTM</b> - <i>{link_utm}</i>\n\n" \
                   f"<b>У вас 3 Фотографии, теперь жмите Добавить</b>"
            media = types.MediaGroup()
            for i in data.get("photo"):
                media.attach_photo(i)
            await bot.send_media_group(message.from_user.id,
                                       media=media)
            await bot.send_message(message.from_user.id,
                                   text,
                                   reply_markup=AdminAddMarkup.admin_add_ozon_finish(),
                                   disable_web_page_preview=True)
        await states.AdminStatesOzon.next()

    @staticmethod
    async def ozon_finish(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            await general_set.product_ozon_add_with_photo(data.get('title'),
                                                          data.get('type_product'),
                                                          int(data.get('article_product')),
                                                          int(data.get('price')),
                                                          "Ссылки нет",
                                                          data.get('link_utm'),
                                                          data.get('photo'))
        try:
            for i in range(0, 6):
                await bot.delete_message(callback.from_user.id, callback.message.message_id - i)
        except:
            pass
        len_product = await general_get.products_ozon_all()
        await bot.send_message(callback.from_user.id,
                               "<b>Товар Ozon успешно добавился!</b>\n"
                               f"<b>Всего товаров - {len(len_product)}</b>",
                               reply_markup=AdminCheckMarkup.admin_check_ozon())
        await state.finish()


class AdminWbAddProduct:

    @staticmethod
    async def admin_wb_add_product(callback: types.CallbackQuery):
        await callback.message.edit_text("Добавляем товар из Wildberries\n"
                                         "Введите <b>Наименование</b>",
                                         reply_markup=AdminAddMarkup.admin_add_wb())
        await states.AdminStatesWb.title.set()

    @staticmethod
    async def title_wb(message: types.Message, state: FSMContext):
        if message.text:
            await state.update_data(title=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите Категорию товара</b>",
                                   reply_markup=AdminAddMarkup.admin_add_wb())
            await states.AdminStatesWb.next()

    @staticmethod
    async def type_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
        if message.text:
            await state.update_data(type_product=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите Артикул Продавца</b>",
                                   reply_markup=AdminAddMarkup.admin_add_wb())
            await states.AdminStatesWb.next()

    @staticmethod
    async def article_seller_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
        if message.text:
            await state.update_data(article_seller=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{type_product}</i>\n"
                                   f"<b>Артикул Продавца</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите Артикул Товара</b>",
                                   reply_markup=AdminAddMarkup.admin_add_wb())
            await states.AdminStatesWb.next()

    @staticmethod
    async def article_product_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_seller = data.get("article_seller")
        if message.text.isdigit():
            await state.update_data(article_product=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{type_product}</i>\n"
                                   f"<b>Артикул Продавца</b> - <i>{article_seller}</i>\n"
                                   f"<b>Артикул Товара</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите цену</b>",
                                   reply_markup=AdminAddMarkup.admin_add_wb(),
                                   disable_web_page_preview=True)
            await states.AdminStatesWb.next()
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Артикул товара должен быть цифрой!</b>",
                                   reply_markup=AdminAddMarkup.admin_add_wb())

    @staticmethod
    async def price_spp_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_seller = data.get("article_seller")
            article_product = data.get("article_product")
        if message.text.isdigit():
            await state.update_data(price_spp=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{type_product}</i>\n"
                                   f"<b>Артикул Продавца</b> - <i>{article_seller}</i>\n"
                                   f"<b>Артикул Товара</b> - <i>{article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь введите ссылку</b>",
                                   reply_markup=AdminAddMarkup.admin_add_wb(),
                                   disable_web_page_preview=True)
            await states.AdminStatesWb.next()
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Цена должна быть цифрой!</b>",
                                   reply_markup=AdminAddMarkup.admin_add_wb())

    @staticmethod
    async def link_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_seller = data.get("article_seller")
            article_product = data.get("article_product")
            price_spp = data.get("price_spp")
            data["photo"] = []
        if message.text:
            await state.update_data(link=message.text)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Наименование</b> - <i>{title}</i>\n"
                                   f"<b>Категория</b> - <i>{type_product}</i>\n"
                                   f"<b>Артикул Продавца</b> - <i>{article_seller}</i>\n"
                                   f"<b>Артикул Товара</b> - <i>{article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{price_spp}</i>\n"
                                   f"<b>Ссылка</b> - <i>{message.text}</i>\n\n"
                                   f"<b>Теперь добавьте Фото (Фото добавляется по одной)</b>",
                                   reply_markup=AdminAddMarkup.admin_add_wb(),
                                   disable_web_page_preview=True)
            await states.AdminStatesWb.next()

    @staticmethod
    async def photo_wb_1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_seller = data.get("article_seller")
            article_product = data.get("article_product")
            price_spp = data.get("price_spp")
            link = data.get("link")
        if message.photo:
            async with state.proxy() as data:
                data.get("photo").append(message.photo[2].file_id)
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
        text = f"<b>Наименование</b> - <i>{title}</i>\n" \
               f"<b>Категория</b> - <i>{type_product}</i>\n" \
               f"<b>Артикул Продавца</b> - <i>{article_seller}</i>\n" \
               f"<b>Артикул Товара</b> - <i>{article_product}</i>\n" \
               f"<b>Цена СПП</b> - <i>{price_spp}</i>\n" \
               f"<b>Ссылка</b> - <i>{link}</i>\n\n" \
               f"<b>У вас 1 Фотография, Вы можете еще добавить 2</b>"
        await message.answer_photo(message.photo[2].file_id,
                                   caption=text,
                                   reply_markup=AdminAddMarkup.admin_add_wb_finish())
        await states.AdminStatesWb.next()

    @staticmethod
    async def photo_wb_2(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_seller = data.get("article_seller")
            article_product = data.get("article_product")
            price_spp = data.get("price_spp")
            link = data.get("link")
            if message.photo:
                data.get("photo").append(message.photo[2].file_id)
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
            text = f"<b>Наименование</b> - <i>{title}</i>\n" \
                   f"<b>Категория</b> - <i>{type_product}</i>\n" \
                   f"<b>Артикул Продавца</b> - <i>{article_seller}</i>\n" \
                   f"<b>Артикул Товара</b> - <i>{article_product}</i>\n" \
                   f"<b>Цена СПП</b> - <i>{price_spp}</i>\n" \
                   f"<b>Ссылка</b> - <i>{link}</i>\n\n" \
                   f"<b>У вас 2 Фотографии, можете добавить еще 1</b>"
            media = types.MediaGroup()
            for i in data.get("photo"):
                media.attach_photo(i)
            await bot.send_media_group(message.from_user.id,
                                       media=media)
            await bot.send_message(message.from_user.id,
                                   text,
                                   reply_markup=AdminAddMarkup.admin_add_wb_finish(),
                                   disable_web_page_preview=True)
            await states.AdminStatesWb.next()

    @staticmethod
    async def photo_wb_3(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_seller = data.get("article_seller")
            article_product = data.get("article_product")
            price_spp = data.get("price_spp")
            link = data.get("link")
            if message.photo:
                data.get("photo").append(message.photo[2].file_id)
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
                await bot.delete_message(message.from_user.id, message.message_id - 2)
                await bot.delete_message(message.from_user.id, message.message_id - 3)
            text = f"<b>Наименование</b> - <i>{title}</i>\n" \
                   f"<b>Категория</b> - <i>{type_product}</i>\n" \
                   f"<b>Артикул Продавца</b> - <i>{article_seller}</i>\n" \
                   f"<b>Артикул Товара</b> - <i>{article_product}</i>\n" \
                   f"<b>Цена СПП</b> - <i>{price_spp}</i>\n" \
                   f"<b>Ссылка</b> - <i>{link}</i>\n\n" \
                   f"<b>У вас 3 Фотографии, теперь жмите Добавить</b>"
            media = types.MediaGroup()
            for i in data.get("photo"):
                media.attach_photo(i)
            await bot.send_media_group(message.from_user.id,
                                       media=media)
            await bot.send_message(message.from_user.id,
                                   text,
                                   reply_markup=AdminAddMarkup.admin_add_wb_finish(),
                                   disable_web_page_preview=True)
        await states.AdminStatesWb.next()

    @staticmethod
    async def wb_finish(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            await general_set.product_wb_add_with_photo(data.get('title'),
                                                        data.get('type_product'),
                                                        data.get('article_seller'),
                                                        int(data.get('article_product')),
                                                        int(data.get('price_spp')),
                                                        data.get('link'),
                                                        data.get('photo'))
        try:
            for i in range(0, 6):
                await bot.delete_message(callback.from_user.id, callback.message.message_id - i)
        except:
            pass
        len_product = await general_get.products_wb_all()
        await bot.send_message(callback.from_user.id,
                               "<b>Товар Wildberries успешно добавился!</b>\n"
                               f"<b>Всего товаров - {len(len_product)}</b>",
                               reply_markup=AdminCheckMarkup.admin_check_wb())
        await state.finish()


class AdminOzonView:

    @staticmethod
    async def admin_ozon_view(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите ID товара Ozon",
                                         reply_markup=AdminViewOzonMarkup.admin_enter_id_ozon())
        await states.AdminChangeOzon.enter_id.set()

    @staticmethod
    async def admin_ozon_change_back(callback: types.CallbackQuery):
        await callback.message.edit_text("<b>Вы в меню Ozon</b>",
                                         reply_markup=AdminCheckMarkup.admin_check_ozon())

    @staticmethod
    async def admin_ozon_enter_id(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        if message.photo:
            async with state.proxy() as data:
                product = data.get("product")
                for i in range(0, 5):
                    try:
                        await bot.delete_message(message.from_user.id, message.message_id - i)
                    except:
                        pass
                max_ = await general_set.product_ozon_add_photo(product.id, message.photo[2].file_id)
                if max_:
                    product = await general_get.product_ozon_select(product.id)
                    media = types.MediaGroup()
                    for i in product.photo:
                        media.attach_photo(i)
                    await bot.send_media_group(message.from_user.id,
                                               media=media)
                    text = "<b>У вас 3 Фотографии</b>\n" \
                           "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                           "<b>Редактировать Товар:</b>"
                    await bot.send_message(message.from_user.id,
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                           f"<b>Ссылка с UTM</b> - <i>{product.link_utm}</i>\n"
                                           f"<b>Клики</b> - <i>{product.click}</i>\n\n" + text,
                                           reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
                else:
                    product = await general_get.product_ozon_select(product.id)
                    media = types.MediaGroup()
                    for i in product.photo:
                        media.attach_photo(i)
                    await bot.send_media_group(message.from_user.id,
                                               media=media)
                    if len(product.photo) >= 3:
                        text = "<b>У вас 3 Фотографии</b>\n" \
                               "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    if len(product.photo) == 2:
                        text = "<b>У вас 2 Фотографии</b>\n" \
                               "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    elif len(product.photo) == 1:
                        text = "<b>У вас 1 Фотография</b>\n" \
                               "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    await bot.send_message(message.from_user.id,
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                           f"<b>Ссылка с UTM</b> - <i>{product.link_utm}</i>\n"
                                           f"<b>Клики</b> - <i>{product.click}</i>\n\n" + text,
                                           reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        elif message.text.isdigit():
            product_id = int(message.text)
            product = await general_get.product_ozon_select(product_id)
            await state.update_data(product=product)
            if product:
                if product.photo:
                    text = ""
                    if len(product.photo) >= 3:
                        text = "<b>У вас 3 Фотографии</b>\n" \
                               "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    elif len(product.photo) == 2:
                        text = "<b>У вас 2 Фотографии</b>\n" \
                               "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    elif len(product.photo) == 1:
                        text = "<b>У вас 1 Фотография</b>\n" \
                               "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                               "<b>Редактировать Товар:</b>"
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
                                           f"<b>Ссылка с UTM</b> - <i>{product.link_utm}</i>\n"
                                           f"<b>Клики</b> - <i>{product.click}</i>\n\n" + text,
                                           reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
                else:
                    await bot.send_message(message.from_user.id,
                                           f"<b>Товар без Фото!</b>\n"
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                           f"<b>Ссылка с UTM</b> - <i>{product.link_utm}</i>\n"
                                           f"<b>Клики</b> - <i>{product.click}</i>\n\n"
                                           f"<b>У вас нет Фотографий!</b>\n"
                                           f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                           reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
            else:
                await bot.send_message(message.from_user.id,
                                       "Товар Ozon не найден!",
                                       reply_markup=AdminCheckMarkup.admin_check_ozon())
        elif not message.text.isdigit():
            await bot.send_message(message.from_user.id,
                                   "Надо ввести цифру!",
                                   reply_markup=AdminCheckMarkup.admin_check_ozon())

    @staticmethod
    async def admin_in_product_ozon_back(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            product = data.get("product")
            if product.photo:
                text = ""
                if len(product.photo) >= 3:
                    text = "<b>У вас 3 Фотографии</b>\n" \
                           "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                           "<b>Редактировать Товар:</b>"
                elif len(product.photo) == 2:
                    text = "<b>У вас 2 Фотографии</b>\n" \
                           "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                           "<b>Редактировать Товар:</b>"
                elif len(product.photo) == 1:
                    text = "<b>У вас 1 Фотография</b>\n" \
                           "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                           "<b>Редактировать Товар:</b>"
                await callback.message.edit_text(f"<b>ID</b> - <i>{product.id}</i>\n"
                                                 f"<b>Название</b> - <i>{product.title}</i>\n"
                                                 f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                                 f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                                 f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                                 f"<b>Ссылка с UTM</b> - <i>{product.link_utm}</i>\n"
                                                 f"<b>Клики</b> - <i>{product.click}</i>\n\n" + text,
                                                 reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
            else:
                await callback.message.edit_text("<b>Товар без Фото!</b>\n"
                                                 f"<b>ID</b> - <i>{product.id}</i>\n"
                                                 f"<b>Название</b> - <i>{product.title}</i>\n"
                                                 f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                                 f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                                 f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                                 f"<b>Ссылка с UTM</b> - <i>{product.link_utm}</i>\n"
                                                 f"<b>Клики</b> - <i>{product.click}</i>\n\n"
                                                 f"<b>У вас нет Фотографий!</b>\n"
                                                 f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                                 reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        await states.AdminChangeOzon.enter_id.set()

    @staticmethod
    async def admin_ozon_change_title(callback: types.CallbackQuery):
        await states.AdminChangeOzon.title.set()
        await callback.message.edit_text("<b>Введите новое Наименование товара</b>",
                                         reply_markup=AdminViewOzonMarkup.admin_in_product_ozon_back())

    @staticmethod
    async def admin_ozon_change_title_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_ozon_change_title(product.id, message.text)
        product_new = await general_get.product_ozon_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        await states.AdminChangeOzon.enter_id.set()

    @staticmethod
    async def admin_ozon_change_type_product(callback: types.CallbackQuery):
        await states.AdminChangeOzon.type_product.set()
        await callback.message.edit_text("<b>Введите новую Категорию товара</b>",
                                         reply_markup=AdminViewOzonMarkup.admin_in_product_ozon_back())

    @staticmethod
    async def admin_ozon_change_type_product_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_ozon_change_type_product(product.id, message.text)
        product_new = await general_get.product_ozon_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        await states.AdminChangeOzon.enter_id.set()

    @staticmethod
    async def admin_ozon_change_article_product(callback: types.CallbackQuery):
        await states.AdminChangeOzon.article_product.set()
        await callback.message.edit_text("<b>Введите новый Артикул товара</b>",
                                         reply_markup=AdminViewOzonMarkup.admin_in_product_ozon_back())

    @staticmethod
    async def admin_ozon_change_article_product_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_ozon_change_article_product(product.id, message.text)
        product_new = await general_get.product_ozon_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        await states.AdminChangeOzon.enter_id.set()

    @staticmethod
    async def admin_ozon_change_price(callback: types.CallbackQuery):
        await states.AdminChangeOzon.price.set()
        await callback.message.edit_text("<b>Введите новую Цену товара</b>",
                                         reply_markup=AdminViewOzonMarkup.admin_in_product_ozon_back())

    @staticmethod
    async def admin_ozon_change_price_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_ozon_change_price(product.id, message.text)
        product_new = await general_get.product_ozon_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        await states.AdminChangeOzon.enter_id.set()

    @staticmethod
    async def admin_ozon_change_link_utm(callback: types.CallbackQuery):
        await states.AdminChangeOzon.link_utm.set()
        await callback.message.edit_text("<b>Введите новую Ссылку UTM</b>",
                                         reply_markup=AdminViewOzonMarkup.admin_in_product_ozon_back())

    @staticmethod
    async def admin_ozon_change_link_utm_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_ozon_change_link_utm(product.id, message.text)
        product_new = await general_get.product_ozon_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product_new.price} руб.</i>\n"
                                   f"<b>Ссылка с UTM</b> - <i>{product_new.link_utm}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewOzonMarkup.admin_in_product_ozon())
        await states.AdminChangeOzon.enter_id.set()


class AdminWbView:

    @staticmethod
    async def admin_wb_view(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите ID товара Wildberries",
                                         reply_markup=AdminViewWbMarkup.admin_enter_id_wb())
        await states.AdminChangeWb.enter_id.set()

    @staticmethod
    async def admin_wb_change_back(callback: types.CallbackQuery):
        await callback.message.edit_text("<b>Вы в меню Wildberries</b>",
                                         reply_markup=AdminCheckMarkup.admin_check_wb())

    @staticmethod
    async def admin_wb_enter_id(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        if message.photo:
            async with state.proxy() as data:
                product = data.get("product")
                for i in range(0, 5):
                    try:
                        await bot.delete_message(message.from_user.id, message.message_id - i)
                    except:
                        pass
                max_ = await general_set.product_wb_add_photo(product.id, message.photo[2].file_id)
                if max_:
                    product = await general_get.product_wb_select(product.id)
                    media = types.MediaGroup()
                    for i in product.photo:
                        media.attach_photo(i)
                    await bot.send_media_group(message.from_user.id,
                                               media=media)
                    text = "<b>У вас 3 Фотографии</b>\n" \
                           "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                           "<b>Редактировать Товар:</b>"
                    await bot.send_message(message.from_user.id,
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул продавца</b> - <i>{product.article_seller}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена СПП</b> - <i>{product.price_spp} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product.link}</i>\n"
                                           f"<b>Клики</b> - <i>{product.click}</i>\n\n" + text,
                                           reply_markup=AdminViewWbMarkup.admin_in_product_wb())
                else:
                    product = await general_get.product_wb_select(product.id)
                    media = types.MediaGroup()
                    for i in product.photo:
                        media.attach_photo(i)
                    await bot.send_media_group(message.from_user.id,
                                               media=media)
                    if len(product.photo) >= 3:
                        text = "<b>У вас 3 Фотографии</b>\n" \
                               "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    if len(product.photo) == 2:
                        text = "<b>У вас 2 Фотографии</b>\n" \
                               "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    elif len(product.photo) == 1:
                        text = "<b>У вас 1 Фотография</b>\n" \
                               "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    await bot.send_message(message.from_user.id,
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул продавца</b> - <i>{product.article_seller}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена СПП</b> - <i>{product.price_spp} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product.link}</i>\n"
                                           f"<b>Клики</b> - <i>{product.click}</i>\n\n" + text,
                                           reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        elif message.text.isdigit():
            product_id = int(message.text)
            product = await general_get.product_wb_select(product_id)
            await state.update_data(product=product)
            if product:
                if product.photo:
                    text = ""
                    if len(product.photo) >= 3:
                        text = "<b>У вас 3 Фотографии</b>\n" \
                               "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    elif len(product.photo) == 2:
                        text = "<b>У вас 2 Фотографии</b>\n" \
                               "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                               "<b>Редактировать Товар:</b>"
                    elif len(product.photo) == 1:
                        text = "<b>У вас 1 Фотография</b>\n" \
                               "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                               "<b>Редактировать Товар:</b>"
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
                                           f"<b>Цена СПП</b> - <i>{product.price_spp} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product.link}</i>\n"
                                           f"<b>Клики</b> - <i>{product.click}</i>\n\n" + text,
                                           reply_markup=AdminViewWbMarkup.admin_in_product_wb())
                else:
                    await bot.send_message(message.from_user.id,
                                           f"<b>Товар без Фото!</b>\n"
                                           f"<b>ID</b> - <i>{product.id}</i>\n"
                                           f"<b>Название</b> - <i>{product.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                           f"<b>Артикул продавца</b> - <i>{product.article_seller}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                           f"<b>Цена СПП</b> - <i>{product.price_spp} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product.link}</i>\n"
                                           f"<b>Клики</b> - <i>{product.click}</i>\n\n"
                                           f"<b>У вас нет Фотографий!</b>\n"
                                           f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                           reply_markup=AdminViewWbMarkup.admin_in_product_wb())
            else:
                await bot.send_message(message.from_user.id,
                                       "Товар Wildberries не найден!",
                                       reply_markup=AdminCheckMarkup.admin_check_wb())
        elif not message.text.isdigit():
            await bot.send_message(message.from_user.id,
                                   "Надо ввести цифру!",
                                   reply_markup=AdminCheckMarkup.admin_check_wb())

    @staticmethod
    async def admin_in_product_wb_back(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            product = data.get("product")
            if product.photo:
                text = ""
                if len(product.photo) >= 3:
                    text = "<b>У вас 3 Фотографии</b>\n" \
                           "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                           "<b>Редактировать Товар:</b>"
                elif len(product.photo) == 2:
                    text = "<b>У вас 2 Фотографии</b>\n" \
                           "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                           "<b>Редактировать Товар:</b>"
                elif len(product.photo) == 1:
                    text = "<b>У вас 1 Фотография</b>\n" \
                           "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                           "<b>Редактировать Товар:</b>"
                await callback.message.edit_text(f"<b>ID</b> - <i>{product.id}</i>\n"
                                                 f"<b>Название</b> - <i>{product.title}</i>\n"
                                                 f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                                 f"<b>Артикул продавца</b> - <i>{product.article_seller}</i>\n"
                                                 f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                                 f"<b>Цена СПП</b> - <i>{product.price_spp} руб.</i>\n"
                                                 f"<b>Ссылка</b> - <i>{product.link}</i>\n"
                                                 f"<b>Клики</b> - <i>{product.click}</i>\n\n" + text,
                                                 reply_markup=AdminViewWbMarkup.admin_in_product_wb())
            else:
                await callback.message.edit_text("<b>Товар без Фото!</b>\n"
                                                 f"<b>ID</b> - <i>{product.id}</i>\n"
                                                 f"<b>Название</b> - <i>{product.title}</i>\n"
                                                 f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                                 f"<b>Артикул продавца</b> - <i>{product.article_seller}</i>\n"
                                                 f"<b>Артикул товара</b> - <i>{product.article_product}</i>\n"
                                                 f"<b>Цена СПП</b> - <i>{product.price_spp} руб.</i>\n"
                                                 f"<b>Ссылка</b> - <i>{product.link}</i>\n"
                                                 f"<b>Клики</b> - <i>{product.click}</i>\n\n"
                                                 f"<b>У вас нет Фотографий!</b>\n"
                                                 f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                                 reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        await states.AdminChangeWb.enter_id.set()

    @staticmethod
    async def admin_wb_change_title(callback: types.CallbackQuery):
        await states.AdminChangeWb.title.set()
        await callback.message.edit_text("<b>Введите новое Наименование товара</b>",
                                         reply_markup=AdminViewWbMarkup.admin_in_product_wb_back())

    @staticmethod
    async def admin_wb_change_title_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_wb_change_title(product.id, message.text)
        product_new = await general_get.product_wb_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        await states.AdminChangeWb.enter_id.set()

    @staticmethod
    async def admin_wb_change_type_product(callback: types.CallbackQuery):
        await states.AdminChangeWb.type_product.set()
        await callback.message.edit_text("<b>Введите новую Категорию товара</b>",
                                         reply_markup=AdminViewWbMarkup.admin_in_product_wb_back())

    @staticmethod
    async def admin_wb_change_type_product_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_wb_change_type_product(product.id, message.text)
        product_new = await general_get.product_wb_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        await states.AdminChangeWb.enter_id.set()

    @staticmethod
    async def admin_wb_change_article_seller(callback: types.CallbackQuery):
        await states.AdminChangeWb.article_seller.set()
        await callback.message.edit_text("<b>Введите новый Артикул продавца</b>",
                                         reply_markup=AdminViewWbMarkup.admin_in_product_wb_back())

    @staticmethod
    async def admin_wb_change_article_seller_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_wb_change_article_seller(product.id, message.text)
        product_new = await general_get.product_wb_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        await states.AdminChangeWb.enter_id.set()

    @staticmethod
    async def admin_wb_change_article_product(callback: types.CallbackQuery):
        await states.AdminChangeWb.article_product.set()
        await callback.message.edit_text("<b>Введите новый Артикул товара</b>",
                                         reply_markup=AdminViewWbMarkup.admin_in_product_wb_back())

    @staticmethod
    async def admin_wb_change_article_product_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_wb_change_article_product(product.id, message.text)
        product_new = await general_get.product_wb_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        await states.AdminChangeWb.enter_id.set()

    @staticmethod
    async def admin_wb_change_price_spp(callback: types.CallbackQuery):
        await states.AdminChangeWb.price_spp.set()
        await callback.message.edit_text("<b>Введите новую Цену СПП товара</b>",
                                         reply_markup=AdminViewWbMarkup.admin_in_product_wb_back())

    @staticmethod
    async def admin_wb_change_price_spp_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_wb_change_price(product.id, message.text)
        product_new = await general_get.product_wb_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        await states.AdminChangeWb.enter_id.set()

    @staticmethod
    async def admin_wb_change_link(callback: types.CallbackQuery):
        await states.AdminChangeWb.link.set()
        await callback.message.edit_text("<b>Введите новую Ссылку</b>",
                                         reply_markup=AdminViewWbMarkup.admin_in_product_wb_back())

    @staticmethod
    async def admin_wb_change_link_(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            product = data.get("product")
            await general_set.product_wb_change_link(product.id, message.text)
        product_new = await general_get.product_wb_select(product.id)
        await state.update_data(product=product_new)
        if product_new.photo:
            text = ""
            if len(product_new.photo) >= 3:
                text = "<b>У вас 3 Фотографии</b>\n" \
                       "<b>Вы не можете добавить сюда Фотографии</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 2:
                text = "<b>У вас 2 Фотографии</b>\n" \
                       "<b>Вы можете добавить сюда 1 Фотографию (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            elif len(product_new.photo) == 1:
                text = "<b>У вас 1 Фотография</b>\n" \
                       "<b>Вы можете добавить сюда 2 Фотографии (Добавлять по 1 Фото)</b>\n" \
                       "<b>Редактировать Товар:</b>"
            await bot.send_message(message.from_user.id,
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n" + text,
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        else:
            await bot.send_message(message.from_user.id,
                                   "<b>Товар без Фото!</b>\n"
                                   f"<b>ID</b> - <i>{product_new.id}</i>\n"
                                   f"<b>Название</b> - <i>{product_new.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product_new.type_product}</i>\n"
                                   f"<b>Артикул продавца</b> - <i>{product_new.article_seller}</i>\n"
                                   f"<b>Артикул товара</b> - <i>{product_new.article_product}</i>\n"
                                   f"<b>Цена СПП</b> - <i>{product_new.price_spp} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product_new.link}</i>\n"
                                   f"<b>Клики</b> - <i>{product_new.click}</i>\n\n"
                                   f"<b>У вас нет Фотографий!</b>\n"
                                   f"<b>Вы можете добавить сюда 3 Фотографии (Добавлять по 1 Фото)</b>",
                                   reply_markup=AdminViewWbMarkup.admin_in_product_wb())
        await states.AdminChangeWb.enter_id.set()
