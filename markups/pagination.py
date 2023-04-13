from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

pagination_call = CallbackData("paginator", "key", "page")
show_item = CallbackData("show_item", "item_id")


def get_pages_keyboard(array, page: int = 1):
    key = "items"
    markup = InlineKeyboardMarkup(row_width=1)
    MAX_ITEMS_PER_PAGE = 1
    first_item_index = (page - 1) * MAX_ITEMS_PER_PAGE
    last_item_index = page * MAX_ITEMS_PER_PAGE

    sliced_array = array[first_item_index:last_item_index]
    item_buttons = list()

    for item in sliced_array:
        item_buttons.append(
            InlineKeyboardButton(
                text=f"{item.name} - ${item.price}",
                callback_data=show_item.new(item_id=item.id)
            )
        )
    pages_buttons = list()
    first_page = 1
    first_page_text = "<< 1"

    max_page = len(array) // MAX_ITEMS_PER_PAGE
    max_page_text = f">> {max_page}"

    pages_buttons.append(
        InlineKeyboardButton(
            text=first_page_text,
            callback_data=pagination_call.new(key=key, page=first_page)
        )
    )
    previous_page = page - 1
    previous_page_text = f"< {previous_page}"

    if previous_page >= first_page:
        pages_buttons.append(
            InlineKeyboardButton(
                text=previous_page_text,
                callback_data=pagination_call.new(key=key,
                                                  page=previous_page)
            )
        )
    else:
        pages_buttons.append(
            InlineKeyboardButton(
                text=" . ",
                callback_data=pagination_call.new(key=key,
                                                  page="current_page")
            )
        )
    pages_buttons.append(
        InlineKeyboardButton(
            text=f"- {page} -",
            callback_data=pagination_call.new(key=key,
                                              page="current_page")
        )
    )

    next_page = page + 1
    next_page_text = f"{next_page} >"

    if next_page <= max_page:
        pages_buttons.append(
            InlineKeyboardButton(
                text=next_page_text,
                callback_data=pagination_call.new(key=key,
                                                  page=next_page)
            )
        )
    else:
        pages_buttons.append(
            InlineKeyboardButton(
                text=" . ",
                callback_data=pagination_call.new(key=key,
                                                  page="current_page")
            )
        )
    pages_buttons.append(
        InlineKeyboardButton(
            text=max_page_text,
            callback_data=pagination_call.new(key=key,
                                              page=max_page)
        )
    )
    for button in item_buttons:
        markup.insert(button)

    markup.row(*pages_buttons)
    return markup
