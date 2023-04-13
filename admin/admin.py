from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile, ParseMode

import states
from bot import bot
from markups import pagination
from data.commands import general_set
from settings import config
from states import AdminStatesOzon


class AdminOzon:
    @staticmethod
    async def title_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["title"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Название</b> - {message.text}\n\n"
                               f"<b>Теперь введите Категорию товара</b>")
        await states.AdminStatesOzon.next()

    @staticmethod
    async def type_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["type_product"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Категория</b> - {message.text}\n\n"
                               f"<b>Теперь введите Артикул</b>")
        await states.AdminStatesOzon.next()

    @staticmethod
    async def article_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["article_product"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Артикул</b> - {message.text}\n\n"
                               f"<b>Теперь введите Цену</b>")
        await states.AdminStatesOzon.next()

    @staticmethod
    async def price_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["price"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Цена</b> - {message.text}\n\n"
                               f"<b>Теперь введите Обычную ссылку (без UTM)</b>")
        await states.AdminStatesOzon.next()

    @staticmethod
    async def link_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["link"] = message.text
        await bot.send_message(message.from_user.id,
                               f"<b>Ссылка</b> - {message.text}\n\n"
                               f"<b>Теперь введите ссылку с UTM</b>")
        await states.AdminStatesOzon.next()

    @staticmethod
    async def link_utm_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["link_utm"] = message.text
            data["photo"] = []
        await bot.send_message(message.from_user.id,
                               f"<b>Ссылка c UTM</b> - {message.text}\n\n"
                               f"<b>Теперь введите ссылку на фото</b>")
        await states.AdminStatesOzon.next()

    @staticmethod
    async def photo_ozon(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data.get("photo").append(message.text)
        await bot.send_message(message.from_user.id,
                               f"<b>Название</b> - {data.get('title')}\n"
                               f"<b>Категория</b> - {data.get('type_product')}\n"
                               f"<b>Артикул</b> - {data.get('article_product')}\n"
                               f"<b>Цена</b> - {data.get('price')}\n"
                               f"<b>Ссылка</b> - {data.get('link')}\n"
                               f"<b>Ссылка</b> UTM - {data.get('link_utm')}\n"
                               f"<b>Фото</b> - {data.get('photo')}\n\n"
                               f"<b>Вы можете еще раз сюда ввести ссылку на Фото чтобы Добавить несколько Фото "
                               f"или нажмите Завершить</b>",
                               reply_markup=pagination.admin_done_ozon(),
                               disable_web_page_preview=True)

    @staticmethod
    async def ozon_finish(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            await general_set.product_ozon_add_with_photo(data.get('title'),
                                                          data.get('type_product'),
                                                          int(data.get('article_product')),
                                                          int(data.get('price')),
                                                          data.get('link'),
                                                          data.get('link_utm'),
                                                          data.get('photo'))
        await bot.send_message(callback.from_user.id,
                               "Товар успешно добавился!")
        await state.finish()
