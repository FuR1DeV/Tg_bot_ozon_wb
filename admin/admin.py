import csv

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile, InputMediaPhoto

import states
from bot import bot
from markups.admin_markup import AdminCheckMarkup, AdminAddMarkup
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
        await callback.message.edit_text(text="<b>Вы в меню Ozon</b>",
                                         reply_markup=AdminCheckMarkup.admin_check_ozon())
        await state.finish()

    @staticmethod
    async def admin_check_ozon_excel(callback: types.CallbackQuery):
        all_products = await general_get.products_ozon_all()
        with open("table_ozon.csv", "w", newline='', encoding="windows_1251") as file:
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
                    book.append(f"<b>ID</b> - <i>{i.id}</i>\n"
                                f"<b>Название</b> - <i>{i.title}</i>\n"
                                f"<b>Категория</b> - <i>{i.type_product}</i>\n"
                                f"<b>Артикул товара</b> - <i>{i.article_product}</i>\n"
                                f"<b>Цена</b> - <i>{i.price} руб.</i>\n"
                                f"<b>Ссылка с UTM</b> - <i>{i.link_utm}</i>\n"
                                f"<b>Фото</b> - <i>{i.photo}</i>\n"
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
                        book.append(f"<b>ID</b> - <i>{i.id}</i>\n"
                                    f"<b>Название</b> - <i>{i.title}</i>\n"
                                    f"<b>Категория</b> - <i>{i.type_product}</i>\n"
                                    f"<b>Артикул товара</b> - <i>{i.article_product}</i>\n"
                                    f"<b>Цена</b> - <i>{i.price} руб.</i>\n"
                                    f"<b>Ссылка с UTM</b> - <i>{i.link_utm}</i>\n"
                                    f"<b>Фото</b> - <i>{i.photo}</i>\n"
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
        await callback.message.edit_text(text="<b>Вы в меню Wildberries</b>",
                                         reply_markup=AdminCheckMarkup.admin_check_wb())
        await state.finish()

    @staticmethod
    async def admin_check_wb_excel(callback: types.CallbackQuery):
        all_products = await general_get.products_wb_all()
        with open("table_wildberries.csv", "w", newline='', encoding="windows_1251") as file:
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
                    book.append(f"<b>ID</b> - <i>{i.id}</i>\n"
                                f"<b>Название</b> - <i>{i.title}</i>\n"
                                f"<b>Категория</b> - <i>{i.type_product}</i>\n"
                                f"<b>Артикул продавца</b> - <i>{i.article_seller}</i>\n"
                                f"<b>Артикул товара</b> - <i>{i.article_product}</i>\n"
                                f"<b>Цена с учетом СПП</b> - <i>{i.price_spp} руб.</i>\n"
                                f"<b>Ссылка</b> - <i>{i.link}</i>\n"
                                f"<b>Фото</b> - <i>{i.photo}</i>\n"
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
                        book.append(f"<b>ID</b> - <i>{i.id}</i>\n"
                                    f"<b>Название</b> - <i>{i.title}</i>\n"
                                    f"<b>Категория</b> - <i>{i.type_product}</i>\n"
                                    f"<b>Артикул продавца</b> - <i>{i.article_seller}</i>\n"
                                    f"<b>Артикул товара</b> - <i>{i.article_product}</i>\n"
                                    f"<b>Цена с учетом СПП</b> - <i>{i.price_spp} руб.</i>\n"
                                    f"<b>Ссылка</b> - <i>{i.link}</i>\n"
                                    f"<b>Фото</b> - <i>{i.photo}</i>\n"
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
        if message.text:
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

    @staticmethod
    async def price_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            title = data.get("title")
            type_product = data.get("type_product")
            article_product = data.get("article_product")
        if message.text:
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
                                   f"<b>Теперь загрузите Фото</b>",
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
               f"<b>Вы можете еще добавить 2 Фото</b>"
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
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
                await bot.delete_message(message.from_user.id, message.message_id - 2)
                await bot.delete_message(message.from_user.id, message.message_id - 3)
            text = f"<b>Наименование</b> - <i>{title}</i>\n" \
                   f"<b>Категория</b> - <i>{type_product}</i>\n" \
                   f"<b>Артикул товара</b> - <i>{article_product}</i>\n" \
                   f"<b>Цена</b> - <i>{price}</i>\n" \
                   f"<b>Ссылка UTM</b> - <i>{link_utm}</i>\n\n" \
                   f"<b>У вас 3 фотографии, теперь жмите Добавить</b>"
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
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.delete_message(callback.from_user.id, callback.message.message_id - 1)
        await bot.delete_message(callback.from_user.id, callback.message.message_id - 2)
        await bot.delete_message(callback.from_user.id, callback.message.message_id - 3)
        await bot.send_message(callback.from_user.id,
                               "Товар Ozon успешно добавился!",
                               reply_markup=AdminCheckMarkup.admin_check_ozon())
        await state.finish()


class AdminWb:
    @staticmethod
    async def title_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["title"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Название</b> - {message.text}\n\n"
                               f"<b>Теперь введите Категорию товара</b>")
        await states.AdminStatesWb.next()

    @staticmethod
    async def type_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["type_product"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Категория</b> - {message.text}\n\n"
                               f"<b>Теперь введите Артикул продавца</b>")
        await states.AdminStatesWb.next()

    @staticmethod
    async def article_seller_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["article_seller"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Артикул продавца</b> - {message.text}\n\n"
                               f"<b>Теперь введите артикул товара</b>")
        await states.AdminStatesWb.next()

    @staticmethod
    async def article_product_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["article_product"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Артикул товара</b> - {message.text}\n\n"
                               f"<b>Теперь введите цену с учетом СПП</b>")
        await states.AdminStatesWb.next()

    @staticmethod
    async def price_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["price_spp"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Цена с учетом СПП</b> - {message.text}\n\n"
                               f"<b>Теперь введите ссылку на товар</b>")
        await states.AdminStatesWb.next()

    @staticmethod
    async def link_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["link"] = message.text
            data["photo"] = []
        await bot.send_message(message.from_user.id,
                               f"<b>Ссылка</b> - {message.text}\n\n"
                               f"<b>Теперь введите ссылку на фото</b>")
        await states.AdminStatesWb.next()

    @staticmethod
    async def photo_wb(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data.get("photo").append(message.text)
        await bot.send_message(message.from_user.id,
                               f"<b>Название</b> - {data.get('title')}\n"
                               f"<b>Категория</b> - {data.get('type_product')}\n"
                               f"<b>Артикул продавца</b> - {data.get('article_seller')}\n"
                               f"<b>Артикул товара</b> - {data.get('article_product')}\n"
                               f"<b>Цена</b> - {data.get('price')}\n"
                               f"<b>Ссылка</b> - {data.get('link')}\n"
                               f"<b>Фото</b> - {data.get('photo')}\n\n"
                               f"<b>Вы можете еще раз сюда ввести ссылку на Фото чтобы Добавить несколько Фото "
                               f"или нажмите Завершить</b>",
                               reply_markup=AdminCheckMarkup.admin_done_wb(),
                               disable_web_page_preview=True)

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
        await bot.send_message(callback.from_user.id,
                               "Товар Wildberries успешно добавился!")
        await state.finish()
