import asyncio

from aiogram import types, executor
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from data.commands import general_set, general_get
from admin import register_admin_handler
from settings import config
from states import AdminStatesOzon, AdminStatesWb
from markups import pagination
from content import get_products_ozon_all, get_item_ozon, get_page_ozon, get_products_ozon_all_text
from markups.pagination import pagination_call, get_page_keyboard, see_all_products_markup


@dp.message_handler(Command("getlink"))
async def deep(message: types.Message):
    await message.answer(
        't.me/GraceHouseTelegramBot?start=1'
    )


@dp.message_handler(Command("start"))
async def show_items_handler(message: types.Message):
    user = await general_get.user_select(message.from_user.id)
    if not user:
        await general_set.user_add(message.from_user.id,
                                   message.from_user.username,
                                   None,
                                   message.from_user.first_name,
                                   message.from_user.last_name)
    product_id = message.text.split()
    if len(product_id) == 2:
        product = product_id[1].split("_")
        if product[0] == "ozon":
            product_ozon = await general_get.product_ozon_select(int(product[1]))
            if product_ozon is None:
                await bot.send_message(message.from_user.id,
                                       "Товар не найден!")
            else:
                await general_set.product_ozon_click(int(product[1]))
                try:
                    media = types.MediaGroup()
                    for i in product_ozon.photo:
                        media.attach_photo(i)
                    await bot.send_media_group(message.from_user.id,
                                               media=media,
                                               )
                    await bot.send_message(message.from_user.id,
                                           f"<b>Название</b> - <i>{product_ozon.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product_ozon.type_product}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product_ozon.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product_ozon.price} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product_ozon.link_utm}</i>\n")
                except:
                    await bot.send_message(message.from_user.id,
                                           f"<b>Название</b> - <i>{product_ozon.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product_ozon.type_product}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product_ozon.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product_ozon.price} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product_ozon.link_utm}</i>\n")
        if product[0] == "wb":
            product_wb = await general_get.product_wb_select(int(product[1]))
            if product_wb is None:
                await bot.send_message(message.from_user.id,
                                       "Товар не найден!")
            else:
                await general_set.product_wb_click(int(product[1]))
                try:
                    media = types.MediaGroup()
                    for i in product_wb.photo:
                        media.attach_photo(i)
                    await bot.send_media_group(message.from_user.id,
                                               media=media,
                                               )
                    await bot.send_message(message.from_user.id,
                                           f"<b>Название</b> - <i>{product_wb.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product_wb.type_product}</i>\n"
                                           f"<b>Артикул продавца</b> - <i>{product_wb.article_seller}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product_wb.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product_wb.price_spp} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product_wb.link}</i>\n")
                except:
                    await bot.send_message(message.from_user.id,
                                           f"<b>Название</b> - <i>{product_wb.title}</i>\n"
                                           f"<b>Категория</b> - <i>{product_wb.type_product}</i>\n"
                                           f"<b>Артикул продавца</b> - <i>{product_wb.article_seller}</i>\n"
                                           f"<b>Артикул товара</b> - <i>{product_wb.article_product}</i>\n"
                                           f"<b>Цена</b> - <i>{product_wb.price_spp} руб.</i>\n"
                                           f"<b>Ссылка</b> - <i>{product_wb.link}</i>\n")
    if len(product_id) == 1:
        await bot.send_message(message.from_user.id,
                               "Пока в разработке")


@dp.message_handler(Command("admin"), state=["*"])
async def admin(message: types.Message, state: FSMContext):
    await state.finish()
    if str(message.from_user.id) in config.ADMIN_ID:
        admin_ = await general_get.admin_select(message.from_user.id)
        if not admin_:
            await general_set.admin_add(message.from_user.id,
                                        message.from_user.username,
                                        message.from_user.first_name,
                                        message.from_user.last_name)
        await bot.send_message(message.from_user.id,
                               "Вы можете просмотреть товары и редактировать их",
                               reply_markup=pagination.admin_check())
    else:
        await bot.send_message(message.from_user.id, "У вас нет прав доступа!")


@dp.message_handler(Command("admin_ozon"), state=["*"])
async def admin_ozon(message: types.Message, state: FSMContext):
    await state.finish()
    if str(message.from_user.id) in config.ADMIN_ID:
        admin_ = await general_get.admin_select(message.from_user.id)
        if not admin_:
            await general_set.admin_add(message.from_user.id,
                                        message.from_user.username,
                                        message.from_user.first_name,
                                        message.from_user.last_name)
        await bot.send_message(message.from_user.id,
                               "Добавляем товар из Ozon\n"
                               "Скиньте Название")
        await AdminStatesOzon.title.set()
    else:
        await bot.send_message(message.from_user.id, "У вас нет прав доступа!")


@dp.message_handler(Command("admin_wb"), state=["*"])
async def admin_wb(message: types.Message, state: FSMContext):
    await state.finish()
    if str(message.from_user.id) in config.ADMIN_ID:
        admin_ = await general_get.admin_select(message.from_user.id)
        if not admin_:
            await general_set.admin_add(message.from_user.id,
                                        message.from_user.username,
                                        message.from_user.first_name,
                                        message.from_user.last_name)
        await bot.send_message(message.from_user.id,
                               "Добавляем товар из Wildberries\n"
                               "Скиньте Название")
        await AdminStatesWb.title.set()
    else:
        await bot.send_message(message.from_user.id, "У вас нет прав доступа!")


# @dp.message_handler(text_contains=f"Посмотреть все товары")
# async def see_all_products(message: types.Message):
#     text = await get_page_ozon()
#     await message.answer(text,
#                          reply_markup=get_page_keyboard(max_pages=len(await get_products_ozon_all_text())))
#
#
# @dp.callback_query_handler(pagination_call.filter(page="current_page"))
# async def current_page_error(call: CallbackQuery):
#     print(call.message.text)
#
#
# @dp.callback_query_handler(pagination_call.filter(key="book"))
# async def show_chosen_page(call: CallbackQuery, callback_data: dict):
#     current_page = int(callback_data.get("page"))
#     text = await get_page_ozon(page=current_page)
#     markup = get_page_keyboard(max_pages=len(await get_products_ozon_all_text()),
#                                page=current_page)
#     await call.message.edit_text(text=text, reply_markup=markup)


# @dp.callback_query_handler(pagination_call.filter(key="items"))
# async def show_chosen_page(call: CallbackQuery, callback_data: dict):
#     await call.answer()
#     items = await get_products_ozon_all()
#     current_page = int(callback_data.get("page"))
#     markup = get_pages_keyboard(items, page=current_page)
#     await call.message.edit_reply_markup(markup)
#
#
# @dp.callback_query_handler(show_item.filter())
# async def show_item(call: CallbackQuery, callback_data: dict):
#     item_id = callback_data.get("item_id")
#     item = await get_item_ozon(item_id=item_id)
#     await call.message.answer(
#         f"Вы выбрали товар №{item.id} - {item.title} "
#         f"По цене: {item.price}"
#     )


async def on_startup(_):
    # asyncio.create_task(scheduler())

    from data import db_gino
    print("Database connected")
    await db_gino.on_startup(dp)

    """Удалить БД"""
    # await db.gino.drop_all()

    """Создание БД"""
    await db_gino.db.gino.create_all()

    """Регистрация хэндлеров"""
    register_admin_handler(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
