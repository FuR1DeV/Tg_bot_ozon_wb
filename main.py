from aiogram import types, executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from data.commands import general_set, general_get
from admin import register_admin_handler
from settings import config
from markups.admin_markup import AdminCheckMarkup


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
                               "<b>Добро пожаловать в меню Администратора</b>\n"
                               "<b>Вы можете просмотреть товары, загружать в Excel, "
                               "редактировать и добавлять новые</b>",
                               reply_markup=AdminCheckMarkup.admin_check())
    else:
        await bot.send_message(message.from_user.id, "У вас нет прав доступа!")


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
