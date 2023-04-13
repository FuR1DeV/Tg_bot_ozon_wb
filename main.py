from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils import executor

from bot import dp
from content import items, get_item
from markups.pagination import get_pages_keyboard, pagination_call, show_item


@dp.message_handler(Command("deeplink"))
async def deep(message: types.Message):
    await message.answer(
        't.me/GraceHouseTelegramBot?start=3'
    )


@dp.message_handler(Command("start"))
async def show_items_handler(message: types.Message):
    try:
        res = message.text.split()
        await message.answer(
            "Вот наши товары",
            reply_markup=get_pages_keyboard(items, page=int(res[1]))
        )
    except:
        await message.answer(
            "Вот наши товары",
            reply_markup=get_pages_keyboard(items)
        )


@dp.callback_query_handler(pagination_call.filter(key="items"))
async def show_chosen_page(call: CallbackQuery, callback_data: dict):
    await call.answer()
    current_page = int(callback_data.get("page"))
    markup = get_pages_keyboard(items, page=current_page)
    await call.message.edit_reply_markup(markup)


@dp.callback_query_handler(show_item.filter())
async def show_item(call: CallbackQuery, callback_data: dict):
    item_id = callback_data.get("item_id")
    item = get_item(item_id=item_id)
    await call.message.answer(
        f"Вы выбрали товар №{item.id} - {item.name} "
        f"По цене: {item.price}"
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
