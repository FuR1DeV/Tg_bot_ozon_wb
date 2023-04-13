import asyncio

from aiogram import types, executor
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from data.commands import general_set, general_get
from admin import register_admin_handler
from states import AdminStatesOzon
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
        product = await general_get.product_ozon_select(int(message.text.split()[1]))
        try:
            media = types.MediaGroup()
            for i in product.photo:
                media.attach_photo(i)
            await bot.send_media_group(message.from_user.id,
                                       media=media,
                                       )
            await bot.send_message(message.from_user.id,
                                   f"<b>Название</b> - <i>{product.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                   f"<b>Артикль товара</b> - <i>{product.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product.link_utm}</i>\n")
        except:
            await bot.send_message(message.from_user.id,
                                   f"<b>Название</b> - <i>{product.title}</i>\n"
                                   f"<b>Категория</b> - <i>{product.type_product}</i>\n"
                                   f"<b>Артикль товара</b> - <i>{product.article_product}</i>\n"
                                   f"<b>Цена</b> - <i>{product.price} руб.</i>\n"
                                   f"<b>Ссылка</b> - <i>{product.link_utm}</i>\n")
    # elif len(product_id) == 1:
    #     items = await get_products_ozon_all()
    #     await bot.send_message(message.from_user.id,
    #                            "У нас есть много выгодных товаров!",
    #                            reply_markup=get_pages_keyboard(items))


@dp.message_handler(Command("admin_ozon"), state=["*"])
async def admin_start(message: types.Message, state: FSMContext):
    admin = await general_get.admin_select(message.from_user.id)
    if not admin:
        await general_set.admin_add(message.from_user.id,
                                    message.from_user.username,
                                    message.from_user.first_name,
                                    message.from_user.last_name)
    await bot.send_message(message.from_user.id,
                           "Добавляем товар из Ozon\n"
                           "Скиньте Название")
    await AdminStatesOzon.title.set()

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
